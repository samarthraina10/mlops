import sys
import subprocess

print("=" * 50)
print("PYTHON INFORMATION")
print("=" * 50)

python_version = sys.version.split()[0]
print("Python Version :", python_version)

print("Python Path    :", sys.executable)



print("\n" + "=" * 50)
print("INSTALLED PYTHON LIBRARIES")
print("=" * 50)

result = subprocess.run(
    [sys.executable, "-m", "pip", "list", "--format=freeze"],
    capture_output=True,
    text=True
)

libraries = [
    line for line in result.stdout.splitlines()
    if line.strip()
]

for library in libraries:
    library_name = library.split("==")[0]
    print(library_name)

print("=" * 50)
print("TOTAL LIBRARIES:", len(libraries))
print("=" * 50)