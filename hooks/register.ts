import type { Register } from 'claude-code'

const MANAGER = /^\/(?:just-do-it:)?justaway(?:\s+(on|off))?\s*$/i
const SCRIPT = 'justdoit-statusline.sh'
// Same resolution as the status line script: CLAUDE_CONFIG_DIR, else ~/.claude.
const configDir = async ($: { env: { get(name: string): Promise<string | undefined> } }) =>
  (await $.env.get('CLAUDE_CONFIG_DIR')) || `${await $.env.get('HOME')}/.claude`
const flagPath = (dir: string, id: string) => `${dir}/.justdoit-manager-${id}`
const quote = (s: string) => `'${s.replace(/'/g, `'\\''`)}'`

export const register: Register = on => {
  // Each session: keeps the status line wrapper script current, and wraps the
  // user's own statusLine command with it unless already wrapped.
  on('session.start', async ($, e, next) => {
    try {
      const dir = await configDir($)
      const script = `${dir}/hooks/${SCRIPT}`
      const settingsPath = `${dir}/settings.json`
      const shipped = await $.fs.read(`${$.plugin.root}/scripts/${SCRIPT}`)
      const installed = await $.fs.read(script).catch(() => '')

      if (installed !== shipped) {
        await $.fs.write(script, shipped)
      }

      // Only a missing file is an empty config; any other read error aborts so
      // the user's settings are never overwritten.
      const raw = await $.fs.read(settingsPath).catch((err: { code?: string }) => {
        if (err?.code === 'ENOENT') return '{}'
        throw err
      })
      const settings = JSON.parse(raw)
      const current: string = settings.statusLine?.command ?? ''

      if (!current.includes(SCRIPT)) {
        settings.statusLine = {
          ...settings.statusLine,
          type: 'command',
          // The user's command runs as one argument, so pipes, `&&` and env
          // prefixes keep binding to it and not to the wrapper.
          command: current
            ? `bash "${script}" bash -c ${quote(current)}`
            : `bash "${script}"`,
        }
        await $.fs.write(settingsPath, `${JSON.stringify(settings, null, 2)}\n`)
      }
    } catch {
      // Status badge is optional; never block the session.
    }

    return next(e)
  })

  on('prompt.submit', async ($, e, next) => {
    const match = MANAGER.exec(e.text.trim())

    if (match) {
      try {
        const isOn = match[1]?.toLowerCase() !== 'off'

        await $.fs.write(flagPath(await configDir($), await $.session.id()), isOn ? 'on' : 'off')
      } catch {
        // Status badge is optional; never block the prompt.
      }
    }

    return next(e)
  })

  // Removes this session's flag file so they do not pile up.
  on('session.end', async ($, e, next) => {
    try {
      await $.process.run(['rm', '-f', flagPath(await configDir($), e.sessionId)])
    } catch {
      // Flag cleanup is best effort.
    }

    return next(e)
  })
}
