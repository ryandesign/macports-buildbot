# macports-buildbot

## Experiment (for performance testing)

In venv, do:

    pip install 'buildbot[bundle]'
    pip install buildbot-macports-custom-views

Create `config.yml`, `workers.yml`, `secrets.yml` and configure using the sample files.

Set `env` and `workdir` in portbuilder and portwatcher factory step(s)
