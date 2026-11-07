# Changelog

## [2.1.0](https://github.com/le0u0/just-do-it/compare/v2.0.0...v2.1.0) (2026-11-07)


### Features

* multi-agent go-review with tiers, verifier and cheap re-review ([33f719f](https://github.com/le0u0/just-do-it/commit/33f719f2ed522e95cb2d6c78ce24d1f058c8f2c4))
* multi-agent go-review with tiers, verifier and triage fetch ([492958b](https://github.com/le0u0/just-do-it/commit/492958b17597aa7018ff90e2850fa7d4365c122c))


### Bug Fixes

* close review gaps found by dogfooding go-review ([4bc6397](https://github.com/le0u0/just-do-it/commit/4bc6397bf8af16a73321a213e5b12030874b190f))

## [2.0.0](https://github.com/le0u0/just-do-it/compare/v1.3.0...v2.0.0) (2026-11-05)


### ⚠ BREAKING CHANGES

* `/start-manager on|off` is now `/justaway on|off`.
* skill names changed, and `/manager on|off` is now `/start-manager on|off`. Skills no longer write plan.md, review.md or triage.md; only the manager saves them.

### Features

* add spec guardrails and red/green evidence to dev-tdd ([1cf5882](https://github.com/le0u0/just-do-it/commit/1cf5882756823d61d5631ebd9a770806081572c3))


### Bug Fixes

* confirm the production change landed before the green run and the commit ([36ae635](https://github.com/le0u0/just-do-it/commit/36ae6350c7fa39493cb8517eedc722a0fe96b7b4))
* make QA template language and Pass/Fail buttons segmented, open links in a new tab ([87f6d19](https://github.com/le0u0/just-do-it/commit/87f6d198427e9f716934fdc442988a86a9d1d227))
* run the spec only after the edit is confirmed, never chained with ; ([74649d7](https://github.com/le0u0/just-do-it/commit/74649d7202100a223f4652d80ded83865116734a))


### Code Refactoring

* rename skills to go-/dev-/start-/to- and make the manager own docs ([4fdf23a](https://github.com/le0u0/just-do-it/commit/4fdf23a05a37e4ce62d791b6d82fae4b0bd1f81d))
* rename start-manager to justaway ([22cd036](https://github.com/le0u0/just-do-it/commit/22cd036e256258e4291e30cda44c75e7e67ef1b7))

## [1.3.0](https://github.com/le0u0/just-do-it/compare/v1.2.0...v1.3.0) (2026-11-05)


### Features

* use playwright-cli in e2e exploration, debugging and runs ([92c4406](https://github.com/le0u0/just-do-it/commit/92c44068521f1ab3ab1138aeb8594b24ac04fb07))


### Bug Fixes

* gate e2e explore through the test on --debug=cli support ([8cff7f1](https://github.com/le0u0/just-do-it/commit/8cff7f1b95022b9d14d1337d0d97a4381476a8a0))

## [1.2.0](https://github.com/le0u0/just-do-it/compare/v1.1.0...v1.2.0) (2026-11-03)


### Features

* show [JUSTDOIT] in status line while manager mode is on ([3d4fe5b](https://github.com/le0u0/just-do-it/commit/3d4fe5b303efa980f347c60a469a9981712af15f))
* show [JUSTDOIT] in status line while manager mode is on ([f8d1630](https://github.com/le0u0/just-do-it/commit/f8d1630f3206f1b6ce98b513ddfcef94e3d81237))

## [1.1.0](https://github.com/le0u0/just-do-it/compare/v1.0.0...v1.1.0) (2026-11-02)


### Features

* merge think into plan and replace agent files with manager-set roles ([458ab36](https://github.com/le0u0/just-do-it/commit/458ab36752c779e1b91da152dbb371cb7a7e36fb))
* merge think into plan, manager-set agent roles, Markdown testing guide with optional HTML ([367a7b6](https://github.com/le0u0/just-do-it/commit/367a7b6b6aa28957d151b432eeb8b29bd2295992))
* testing-guide builds a single bilingual HTML QA page ([5948d9d](https://github.com/le0u0/just-do-it/commit/5948d9da9bed9e8b517e7fc5b7a67eecf9380463))
* tighten plan steps, follow-up commits, review tests and PR opening ([804d11b](https://github.com/le0u0/just-do-it/commit/804d11b4586acb504442576bab99f75bc464fe09))


### Bug Fixes

* testing-guide writes Markdown first, HTML only on request ([e768cd5](https://github.com/le0u0/just-do-it/commit/e768cd5917ca7491dc7a75df36f99e411ff040bb))

## 1.0.0 (2026-10-27)


### Features

* migrate agent-workflow plugin as just-do-it ([dc6fef2](https://github.com/le0u0/just-do-it/commit/dc6fef2b9cc00b759a0c7e016a66fd52f149cf97))
* migrate agent-workflow plugin from le0u0/plugins ([e7a3ff4](https://github.com/le0u0/just-do-it/commit/e7a3ff4b339f9e95d0fe8aef9b502bb82dd833c6))
* rename plugin to just-do-it, reset version to 1.0.0 ([d796456](https://github.com/le0u0/just-do-it/commit/d7964565476a419ca28ebf699f829bd8f79b3351))
