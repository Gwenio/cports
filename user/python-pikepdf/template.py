pkgname = "python-pikepdf"
pkgver = "10.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-pybind11",
    "python-setuptools",
]
makedepends = [
    "ninja",
    "python-devel",
    "python-nanobind-devel",
    "python-scikit_build_core",
    "qpdf-devel",
]
depends = ["python-pillow", "python-lxml"]
checkdepends = [
    "python-hypothesis",
    "python-numpy",
    "python-psutil",
    "python-pytest",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Python library for reading and writing PDF files"
license = "MPL-2.0"
url = "https://github.com/pikepdf/pikepdf"
source = (
    f"https://github.com/pikepdf/pikepdf/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "57c83d6f5fce11ed852a20d1ca33c3a651dd45ab0e893d65b18a3a1620f6c010"
