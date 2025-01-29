Multimodal Epigenetic Sequence Analysis (MESA)
==========

Modality perforamce evaluation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``circula mesa`` with ``-p`` option will perform modality performance evaluation. To get a glance of the performance of each modality in terms of classification, the program will test classifier(s) for each modality with cross-validation. 
To quickly assess the perforamnce, the ``--subset`` option can be used to specify the number or ratio of samples to be used for the evaluation, which will randomly sample features for each modality accordingly. The ``--repeat`` option can be used to specify the number of repeats for the random test. 
The ``--clf`` option can be used to specify the classifier(s) to be used for the evaluation: 1. Random Forest, 2.Logistic Regression, 3. SVM. The ``--label`` option is required to specify the label file. The ``--modality`` option is required to specify the modality name of each input matrix. See :doc:'../api/mesa' for more details.


.. code-block:: bash

   circula mesa \
    ./data/mesa_test_DHS_matrix.tsv \
    ./data/mesa_test_CGI_matrix.tsv \
    ./data/mesa_test_OCC_matrix.tsv \
    ./data/mesa_test_WPS_matrix.tsv \
    --label ./data/mesa_test_label.tsv \
    --modality "DHS meth" "CGI meth" "Occupancy" "WPS" \
    --clf 1 2 3 \
    -p \
    --subset 10000 \
    --repeat 10 \
    -o ./output


.. csv-table:: mesa_modality_performance.tsv
   :file: ./mesa_modality_performance.tsv
   :header-rows: 1
   :align: center
   :delim: |


MESA cross-validation
^^^^^^^^^^^^^^^^^^^^^
For the sake of model fine-tuning and evaluation, ``circula mesa`` with ``--cv_mesa`` option will perform cross-validation automatically for the MESA model based on the input moadlity matrix(s), feature size to select ``--size``, classifier ``--clf``, etc. 
This process will output the cross-validation AUC to ``stdout``.

.. code-block:: bash

   # single modality
   circula mesa ./data/mesa_test_DHS_matrix.tsv --label ./data/20241217_mesa_test_label.tsv --cv

.. code-block:: text

   @Tue Jan 28 23:53:01 2025       MESA.
   @Tue Jan 28 23:53:01 2025       Loading modality(s) matrix from input: ['./data/mesa_test_DHS_matrix.tsv']
   @Tue Jan 28 23:53:02 2025       Classifier for each modality is specified.
   @Tue Jan 28 23:53:02 2025       [RandomForestClassifier(n_jobs=-1, random_state=0)]
   @Tue Jan 28 23:53:02 2025       Loading label from input: ./data/20241217_mesa_test_label.tsv
   @Tue Jan 28 23:53:02 2025       MESA cross-validation for one modality.
   @Tue Jan 28 23:53:02 2025       Single modality input
   @Tue Jan 28 23:55:11 2025       MESA cross-validation AUC: 0.7

Or test multiple modalities with multiple input matrices.

.. code-block:: bash

   # single modality
   circula mesa ./data/mesa_test_DHS_matrix.tsv ./data/mesa_test_CGI_matrix.tsv --label ./data/20241217_mesa_test_label.tsv --cv

.. code-block:: text

   @Tue Jan 28 23:58:12 2025       MESA.
   @Tue Jan 28 23:58:12 2025       Loading modality(s) matrix from input: ['./data/20241217_mesa_test_DHS.tsv', './data/20241217_mesa_test_CGI.tsv']
   @Tue Jan 28 23:58:14 2025       Number of classifier > or < number of modality(s). Use first classifer for all modality(s).
   @Tue Jan 28 23:58:14 2025       RandomForestClassifier(n_jobs=-1, random_state=0)
   @Tue Jan 28 23:58:14 2025       Loading label from input: ./data/20241217_mesa_test_label.tsv
   @Tue Jan 28 23:58:14 2025       MESA cross-validation for multiple modalities.
   @Tue Jan 28 23:58:14 2025       Mutiple modalities input
   @Tue Jan 28 23:55:11 2025       MESA cross-validation AUC: 0.76

MESA construction
^^^^^^^^^^^^^^^^^^^^^
Users can construct a MESA model with ``circula mesa`` with ``--mesa`` option. This process will output the trained MESA model object, in the format of ``.pkl``, to the specified output directory.

.. code-block:: bash

   # multi modality
   circula mesa \
    ./data/mesa_test_DHS_matrix.tsv \
    ./data/mesa_test_CGI_matrix.tsv \
    ./data/mesa_test_OCC_matrix.tsv \
    ./data/mesa_test_WPS_matrix.tsv \
    --label ./data/mesa_test_label.tsv \
    --modality "DHS meth" "CGI meth" "Occupancy" "WPS" \
    --mesa \
    -o ./output

.. code-block:: text

   @Wed Jan 29 00:07:36 2025       MESA.
   @Wed Jan 29 00:07:36 2025       Constructing MESA model.
   @Wed Jan 29 00:07:36 2025       Modality performance test skipped. Loading modality(s) matrix from input: ['./data/mesa_test_DHS_matrix.tsv', './data/mesa_test_CGI_matrix.tsv', './data/mesa_test_OCC_matrix.tsv', './data/mesa_test_WPS_matrix.tsv']
   @Wed Jan 29 00:07:44 2025       Number of classifier > or < number of modality(s). Use first classifer for all modality(s).
   @Wed Jan 29 00:07:44 2025       RandomForestClassifier(n_jobs=-1, random_state=0)
   @Wed Jan 29 00:07:44 2025       Loading label from input: ./data/mesa_test_label.tsv
   @Wed Jan 29 00:07:44 2025       Fitting base estimators.
   ...
   @Wed Jan 29 00:07:44 2025       MESA model saved to ./output/MESA_model.pkl

If ``-p`` option is specified together with ``--mesa``, the program will perform modality performance evaluation and construct the MESA model automatically based on the best-performing modality(s).

.. code-block:: bash

   # multi modality
   circula mesa \
    ./data/mesa_test_DHS_matrix.tsv \
    ./data/mesa_test_CGI_matrix.tsv \
    ./data/mesa_test_OCC_matrix.tsv \
    ./data/mesa_test_WPS_matrix.tsv \
    --label ./data/mesa_test_label.tsv \
    --modality "DHS meth" "CGI meth" "Occupancy" "WPS" \
    --clf 1 2 3 \
    -p --mesa --max_modality 2 \
    --subset 10000 \
    --repeat 10 \
    -o ./output

.. note::
   
   For more information on the available arguments for each step, check :doc:`api` section or check with ``--help``.
