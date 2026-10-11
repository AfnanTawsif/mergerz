"""Development/test launcher for the cooking directory.

Test mode intentionally loads icons/ and fonts/ from the current working directory.
The installed Mergerz application does not use this launcher; its installed command
uses the package's bundled resources instead.
"""

import os

# This must be set before importing mergerz.module because the resource mode is
# determined when module.py is imported.
os.environ["MERGERZ_TEST_MODE"] = "1"

from mergerz.module import main


if __name__ == "__main__":
    main()
