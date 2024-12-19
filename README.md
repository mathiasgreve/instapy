# Instapy

Instapy is an image converter that convertes your JPEG to a greyscale or sepia version.

It is a python package with a provided command line interface.

## Setting Up the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git

2. Navigate to the project directory and create a virtual environment:
   ```bash
   cd your-repo
   python3 -m venv venv

3. Activate the virtual environment:
- macOS/Linux:
  ```bash
  source venv/bin/activate

4. Install the dependencies:
    ```bash
    python3 -m pip install .

## Use command line interface

After successfull installation the functionality can be accessed through the command line interface that is provided:

   ```bash
   instapy <file to convert> <arguments>
   ```

Here are the arguments: 
   ```bash
     -o, --out             The output filename
     -g, --gray            Select gray filter
     -se, --sepia          Select sepia filter
     -sc, --scale
                           Scale factor to resize image
     -i {python,numba,numpy,cython}, --implementation {python,numba,numpy,cython}
                           The implementation
   ```
(NB! cython is NOT implemented yet!!)


