> **tags**: [docker, bash]

# How to configure docker bash completion on Mac

Run the next commands to add complitoin to `docker`, `docker-machine` and `docker-compose`:
```
cd $(brew --prefix)/etc/bash_completion.d
ln -s /Applications/Docker.app/Contents/Resources/etc/docker.bash-completion
ln -s /Applications/Docker.app/Contents/Resources/etc/docker-machine.bash-completion
ln -s /Applications/Docker.app/Contents/Resources/etc/docker-compose.bash-completion
```

or like in official docker doc (both approaches are equal):
```
etc=/Applications/Docker.app/Contents/Resources/etc
ln -s $etc/docker.bash-completion $(brew --prefix)/etc/bash_completion.d/docker
ln -s $etc/docker-machine.bash-completion $(brew --prefix)/etc/bash_completion.d/docker-machine
ln -s $etc/docker-compose.bash-completion $(brew --prefix)/etc/bash_completion.d/docker-compose
```

We assume that `.bash_profile` has the next lines:
```
if [ -f $(brew --prefix)/etc/bash_completion ]; then
    . $(brew --prefix)/etc/bash_completion
fi
```

## References
- [Official Docker Docs](https://docs.docker.com/docker-for-mac/#bash)
- https://blog.alexellis.io/docker-mac-bash-completion/
