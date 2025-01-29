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
   :file: ./ mesa_modality_performance.tsv
   :header-rows: 1
   :align: center