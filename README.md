# az-ai

## CLI Design Notes / Roadmap

### AZD Hooks

- `az-ai hook pre* checks`
- `az-ai hook post* smoke-tests`
- `az-ai hook preprovision auth`
- `az-ai hook postprovision auth`
- `az-ai hook postprovision ingestion`

Example `azure.yaml`:
```yaml
name: az-ai-kickstarter
services:
  backend:
    language: python
    project: src/backend
    host: containerapp
    docker:
      path: ./Dockerfile
      remoteBuild: true
hooks:
  preprovision:
    windows:
      shell: pwsh
      run: uvx az-ai hook preprovision
      interactive: true
      continueOnError: false
    posix:
      shell: sh
      run: uvx az-ai hook preprovision
      interactive: true
      continueOnError: false
```

### Generator

Initial scaffolding:
- `az-ai generator ./my-awesome-app`

Within an app directory:
- `az-ai generator agent --name toto --tools a,b,c`
- `az-ai generator tool --name tutu --functions a,b,c`
- `az-ai generator ingestion ...`
- `az-ai generator model-deployment ...`
- `az-ai generator app-insights workbook` ?

### Misc tools

- `az-ai logs tail`
- `az-ai logs show`
- `az-ai deployment show`?
