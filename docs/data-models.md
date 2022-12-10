# Music microservice

### Song

| Property | Type | unique |
|--------|--------| -----|
| name | string | no
| artist | string | no
| uri | string | yes


### Playlist

| Property | Type | unique |
|--------|--------| -----|
| name | string | no
| songs | list | no
| comments | string | no

The playlist contains a list of songs with the data shape from the Song model.


# Accounts microservice

### User

| Property | Type | unique |
|--------|--------| -----|
| full_name | string | no
| username | string | no
| password | string | no
