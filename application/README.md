# Sample kiosk application

Build the container image.

```sh
podman build -t localhost/kiosk-app:latest .
```

Run the container image.

```sh
podman run -it --rm --name kiosk-app -p 5000:5000 localhost/kiosk-app:latest
```

Test it.

```sh
curl -I http://localhost:5000/
```

Login to the registry.

```sh
podman login quay.io
```

Publish it to the registry.

```sh
podman tag localhost/kiosk-app:latest quay.io/nmasse_itix/kiosk-app:latest
podman push quay.io/nmasse_itix/kiosk-app:latest
```