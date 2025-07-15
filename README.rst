Best Practices for Developing Monte Carlo Methodologies in Molecular Simulations v1.0
************************************************************************************************************

This repository contains all the files needed to create the manuscript "Best Practices for Developing Monte Carlo Methodologies in Molecular Simulations v1.0"

See the releases folder for a PDF of the manuscript.

The figures may be generated as follows:

.. code-block:: bash

   pushd figures
   pip install numpy matplotlib
   bash compile_figs.sh
   popd

The PDF may be generated as follows:

.. code-block:: bash

   pushd paper
   sudo [apt/dnf/brew] install texlive
   bash recompile.sh
   popd

The ideal gas tests can be run as follows:

.. code-block:: bash

   pushd codes
   bash run_all_tests.sh
   popd

Some codes files are redundant with figure files.
This is intentional, because code blocks present in the manuscript are shortened to fit the page.

Disclaimer
================================================================================

Certain commercial firms and trade names are identified in this document in order to specify the installation and usage procedures adequately. Such identification is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that related products are necessarily the best available for the purpose.
