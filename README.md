# Python and Shell utility scripts

[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.1252220.svg)](https://zenodo.org/record/1252220)
[![PyPi Download stats](http://pepy.tech/badge/pybashutils)](http://pepy.tech/project/pybashutils)

Collection of Bash and Python scripts I've made that may be generally
useful

  function       |   description
-----------------|-------------------------------------------------------------
  checkIP        |  Sends you an email automatically if your IP address changes
  getIP          |  gets your public IP address (not the internal NAT address)
  mx             |  mount network share example using SSHFS
  memfree        |  Estimates available RAM
  doc2pdf        |  convert .doc, .docx, .rtf to PDF using LibreOffice

## Usage

### SSHFS mount/unmount

1. Mounting the "U" network drive at Boston University over SSHFS
    (slight modifications to the script allow using this anywhere)

    one time setup:

        mkdir ~/U

2. mount U drive to your PC, like "mounting a network drive" in
    Windows, here we assume the BU username is `jdoe`:

        mU jdoe

and your network drive is available as ~/U

3. Unmounting the "U" drive. When done for the day, suggest unmounting
    in case to help mitigate security risks:

        uU

Note: if you have any files open (like say a spreadsheet on the `~/U`
drive), `~/U` will stay connected until you close that file(s).

---

Get Public IP address

```sh
python getIP.py
```
