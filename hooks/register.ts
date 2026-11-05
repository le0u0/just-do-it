import type { Register } from 'claude-code'

const MANAGER = /^\/(?:just-do-it:)?start-manager(?:\s+(on|off))?\s*$/i
const SCRIPT = 'justdoit-statusline.sh'
const flagPath = (home: string | undefined, id: string) =>
  `${home}/.claude/.justdoit-manager-${id}`

export const register: Register = on => {
  // Each session: keeps the status line wrapper script current, and wraps the
  // user's own statusLine command with it unless already wrapped.
  on('session.start', async ($, e, next) => {
    try {
      const home = await $.env.get('HOME')
      const script = `${home}/.claude/hooks/${SCRIPT}`
      const settingsPath = `${home}/.claude/settings.json`
      const shipped = await $.fs.read(`${$.plugin.root}/scripts/${SCRIPT}`)
      const installed = await $.fs.read(script).catch(() => '')

      if (installed !== shipped) {
        await $.fs.write(script, shipped)
      }

      const settings = JSON.parse(await $.fs.read(settingsPath).catch(() => '{}'))
      const current: string = settings.statusLine?.command ?? ''

      if (!current.includes(SCRIPT)) {
        settings.statusLine = {
          ...settings.statusLine,
          type: 'command',
          command: `bash "${script}" ${current}`.trim(),
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
      const home = await $.env.get('HOME')
      const isOn = match[1]?.toLowerCase() !== 'off'

      await $.fs.write(flagPath(home, await $.session.id()), isOn ? 'on' : 'off')
    }

    return next(e)
  })

  // Removes this session's flag file so they do not pile up.
  on('session.end', async ($, e, next) => {
    const home = await $.env.get('HOME')
    await $.process.run(['rm', '-f', flagPath(home, e.sessionId)]).catch(() => {})

    return next(e)
  })
}
