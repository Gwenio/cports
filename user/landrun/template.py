pkgname = "landrun"
pkgver = "0.1.14"
pkgrel = 0
build_style = "go"
make_build_args = [
    "./cmd/landrun",
]
hostmakedepends = ["go"]
pkgdesc = "Sandbox for running processes using Landlock"
license = "MIT"
url = "https://github.com/Zouuup/landrun"
source = f"https://github.com/Zouuup/landrun/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4f943fa39cd2741240f2f114eb97350a99813ea15a9aedc59c87c86df497809e"


def post_install(self):
    self.install_license("LICENSE")
