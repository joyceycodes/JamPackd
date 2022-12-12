# Music microservice

### Song

| Field | Type | Unique |
|--------|--------| -----|
| name | string | no
| artist | string | no
| uri | string | yes


### Playlist

| Field | Type | Unique |
|--------|--------| -----|
| name | string | no
| songs | list | no
| comments | string | no

The playlist contains a list of songs with the data shape from the Song model.


# Accounts microservice

### User

| Field | Type | Unique |
|--------|--------| -----|
| full_name | string | no
| username | string | no
| password | string | no
