{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "V5E1",
      "authorship_tag": "ABX9TyNAzCgzEI1AIb7hbSsKshzy",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "TPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sarony-2002/streamlit-workshop-template/blob/main/HiStudent1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit --ignore-installed"
      ],
      "metadata": {
        "id": "k9WCWviVdjv9",
        "outputId": "240df5ae-05ef-480d-8c1d-c90fe99b3881",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.60.0-py3-none-any.whl.metadata (10 kB)\n",
            "Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit)\n",
            "  Downloading altair-6.2.2-py3-none-any.whl.metadata (11 kB)\n",
            "Collecting blinker<2,>=1.5.0 (from streamlit)\n",
            "  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
            "Collecting click<9,>=7.0 (from streamlit)\n",
            "  Downloading click-8.4.2-py3-none-any.whl.metadata (2.6 kB)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading gitpython-3.1.56-py3-none-any.whl.metadata (14 kB)\n",
            "Collecting numpy<3,>=1.23 (from streamlit)\n",
            "  Downloading numpy-2.5.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)\n",
            "Collecting packaging>=20 (from streamlit)\n",
            "  Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)\n",
            "Collecting pandas<4,>=1.4.0 (from streamlit)\n",
            "  Downloading pandas-3.0.5-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.5/79.5 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pillow<13,>=7.1.0 (from streamlit)\n",
            "  Downloading pillow-12.3.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.1 kB)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.3-py2.py3-none-any.whl.metadata (4.2 kB)\n",
            "Collecting protobuf<8,>=3.20 (from streamlit)\n",
            "  Downloading protobuf-7.35.1-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)\n",
            "Collecting pyarrow<25,>=7.0 (from streamlit)\n",
            "  Downloading pyarrow-24.0.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.0 kB)\n",
            "Collecting requests<3,>=2.27 (from streamlit)\n",
            "  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)\n",
            "Collecting tenacity<10,>=8.1.0 (from streamlit)\n",
            "  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)\n",
            "Collecting toml<2,>=0.10.1 (from streamlit)\n",
            "  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)\n",
            "Collecting typing-extensions<5,>=4.10.0 (from streamlit)\n",
            "  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)\n",
            "Collecting starlette<2,>=0.40.0 (from streamlit)\n",
            "  Downloading starlette-1.3.1-py3-none-any.whl.metadata (6.4 kB)\n",
            "Collecting uvicorn<1,>=0.30.0 (from streamlit)\n",
            "  Downloading uvicorn-0.51.0-py3-none-any.whl.metadata (6.6 kB)\n",
            "Collecting httptools<1,>=0.6.3 (from streamlit)\n",
            "  Downloading httptools-0.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)\n",
            "Collecting anyio<5,>=4.0.0 (from streamlit)\n",
            "  Downloading anyio-4.14.2-py3-none-any.whl.metadata (4.6 kB)\n",
            "Collecting python-multipart<1,>=0.0.10 (from streamlit)\n",
            "  Downloading python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)\n",
            "Collecting websockets<17,>=12.0.0 (from streamlit)\n",
            "  Downloading websockets-16.1.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)\n",
            "Collecting itsdangerous<3,>=2.1.2 (from streamlit)\n",
            "  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m4.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)\n",
            "Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)\n",
            "Collecting narwhals>=2.4.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading narwhals-2.24.0-py3-none-any.whl.metadata (15 kB)\n",
            "Collecting idna>=2.8 (from anyio<5,>=4.0.0->streamlit)\n",
            "  Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)\n",
            "Collecting python-dateutil>=2.8.2 (from pandas<4,>=1.4.0->streamlit)\n",
            "  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)\n",
            "Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)\n",
            "  Downloading charset_normalizer-3.4.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (41 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.7/41.7 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting urllib3<3,>=1.26 (from requests<3,>=2.27->streamlit)\n",
            "  Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)\n",
            "Collecting certifi>=2023.5.7 (from requests<3,>=2.27->streamlit)\n",
            "  Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)\n",
            "Collecting h11>=0.8 (from uvicorn<1,>=0.30.0->streamlit)\n",
            "  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)\n",
            "Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)\n",
            "Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)\n",
            "Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)\n",
            "Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)\n",
            "Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
            "  Downloading rpds_py-2026.6.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)\n",
            "Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit)\n",
            "  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)\n",
            "Downloading streamlit-1.60.0-py3-none-any.whl (10.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.4/10.4 MB\u001b[0m \u001b[31m95.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading altair-6.2.2-py3-none-any.whl (797 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m797.6/797.6 kB\u001b[0m \u001b[31m56.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading anyio-4.14.2-py3-none-any.whl (125 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m125.8/125.8 kB\u001b[0m \u001b[31m13.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
            "Downloading click-8.4.2-py3-none-any.whl (119 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m119.2/119.2 kB\u001b[0m \u001b[31m11.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitpython-3.1.56-py3-none-any.whl (216 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m216.6/216.6 kB\u001b[0m \u001b[31m19.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httptools-0.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (523 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m523.9/523.9 kB\u001b[0m \u001b[31m41.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)\n",
            "Downloading numpy-2.5.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m16.7/16.7 MB\u001b[0m \u001b[31m166.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading packaging-26.2-py3-none-any.whl (100 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m100.2/100.2 kB\u001b[0m \u001b[31m10.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pandas-3.0.5-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.0/11.0 MB\u001b[0m \u001b[31m174.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pillow-12.3.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m140.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading protobuf-7.35.1-cp310-abi3-manylinux2014_x86_64.whl (327 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m327.1/327.1 kB\u001b[0m \u001b[31m31.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pyarrow-24.0.0-cp312-cp312-manylinux_2_28_x86_64.whl (48.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.9/48.9 MB\u001b[0m \u001b[31m30.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.3-py2.py3-none-any.whl (11.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.4/11.4 MB\u001b[0m \u001b[31m121.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_multipart-0.0.32-py3-none-any.whl (30 kB)\n",
            "Downloading requests-2.34.2-py3-none-any.whl (73 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.1/73.1 kB\u001b[0m \u001b[31m7.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading starlette-1.3.1-py3-none-any.whl (73 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.6/73.6 kB\u001b[0m \u001b[31m7.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tenacity-9.1.4-py3-none-any.whl (28 kB)\n",
            "Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
            "Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m45.6/45.6 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading uvicorn-0.51.0-py3-none-any.whl (73 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.2/73.2 kB\u001b[0m \u001b[31m7.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m8.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading websockets-16.1.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (187 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m187.1/187.1 kB\u001b[0m \u001b[31m20.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading certifi-2026.7.22-py3-none-any.whl (136 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m137.0/137.0 kB\u001b[0m \u001b[31m14.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading charset_normalizer-3.4.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (224 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m224.3/224.3 kB\u001b[0m \u001b[31m23.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitdb-4.0.12-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.8/62.8 kB\u001b[0m \u001b[31m6.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading h11-0.16.0-py3-none-any.whl (37 kB)\n",
            "Downloading idna-3.18-py3-none-any.whl (65 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m65.5/65.5 kB\u001b[0m \u001b[31m7.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jinja2-3.1.6-py3-none-any.whl (134 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m134.9/134.9 kB\u001b[0m \u001b[31m12.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonschema-4.26.0-py3-none-any.whl (90 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m90.6/90.6 kB\u001b[0m \u001b[31m8.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading narwhals-2.24.0-py3-none-any.whl (461 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m461.0/461.0 kB\u001b[0m \u001b[31m44.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m229.9/229.9 kB\u001b[0m \u001b[31m23.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading urllib3-2.7.0-py3-none-any.whl (131 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m131.1/131.1 kB\u001b[0m \u001b[31m14.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading attrs-26.1.0-py3-none-any.whl (67 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.5/67.5 kB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)\n",
            "Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)\n",
            "Downloading referencing-0.37.0-py3-none-any.whl (26 kB)\n",
            "Downloading rpds_py-2026.6.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (366 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m366.2/366.2 kB\u001b[0m \u001b[31m34.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading six-1.17.0-py2.py3-none-any.whl (11 kB)\n",
            "Downloading smmap-5.0.3-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: websockets, watchdog, urllib3, typing-extensions, toml, tenacity, smmap, six, rpds-py, python-multipart, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, itsdangerous, idna, httptools, h11, click, charset_normalizer, certifi, blinker, attrs, uvicorn, requests, referencing, python-dateutil, jinja2, gitdb, anyio, starlette, pydeck, pandas, jsonschema-specifications, gitpython, jsonschema, altair, streamlit\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires pandas==2.2.2, but you have pandas 3.0.5 which is incompatible.\n",
            "google-colab 1.0.0 requires requests==2.32.4, but you have requests 2.34.2 which is incompatible.\n",
            "numba 0.66.0 requires numpy<2.5,>=1.22, but you have numpy 2.5.1 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed MarkupSafe-3.0.3 altair-6.2.2 anyio-4.14.2 attrs-26.1.0 blinker-1.9.0 certifi-2026.7.22 charset_normalizer-3.4.9 click-8.4.2 gitdb-4.0.12 gitpython-3.1.56 h11-0.16.0 httptools-0.8.0 idna-3.18 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 narwhals-2.24.0 numpy-2.5.1 packaging-26.2 pandas-3.0.5 pillow-12.3.0 protobuf-7.35.1 pyarrow-24.0.0 pydeck-0.9.3 python-dateutil-2.9.0.post0 python-multipart-0.0.32 referencing-0.37.0 requests-2.34.2 rpds-py-2026.6.3 six-1.17.0 smmap-5.0.3 starlette-1.3.1 streamlit-1.60.0 tenacity-9.1.4 toml-0.10.2 typing-extensions-4.16.0 urllib3-2.7.0 uvicorn-0.51.0 watchdog-6.0.0 websockets-16.1.1\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "PIL",
                  "certifi",
                  "dateutil",
                  "google",
                  "numpy",
                  "packaging",
                  "six"
                ]
              },
              "id": "6711fdbab95b4abb8e9db065128bdfa4"
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sDpUJ2-UnjKe",
        "outputId": "5b78d7a3-3c2b-4d9c-e59a-f02a038aace6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-07-25 18:09:09.124 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.274 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2026-07-25 18:09:09.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.276 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.276 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.276 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.277 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.277 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.277 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.278 Session state does not function when running a script without `streamlit run`\n",
            "2026-07-25 18:09:09.278 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.278 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.279 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.279 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.279 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.280 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.280 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.280 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.281 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.281 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:09.282 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:10.639 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:10.640 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-25 18:09:10.640 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "st.title(\"🚀 My First Cross-Major Streamlit App\")\n",
        "st.write(\"Welcome! Modify the widgets below to see how interactive web apps work.\")\n",
        "\n",
        "user_name = st.text_input(\"What is your name?\", \"Student\")\n",
        "st.subheader(f\"Hello, {user_name}! 👋\")\n",
        "\n",
        "number = st.slider(\"Select a number of data points\", 10, 100, 50)\n",
        "\n",
        "data = pd.DataFrame(\n",
        "    np.random.randn(number, 2),\n",
        "    columns=['X Factor', 'Y Factor']\n",
        ")\n",
        "\n",
        "st.line_chart(data)"
      ]
    }
  ]
}