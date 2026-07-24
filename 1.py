{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "V5E1",
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
        "<a href=\"https://colab.research.google.com/github/Sarony-2002/streamlit-workshop-template/blob/main/1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R8C11yB8vOST",
        "outputId": "c0ec9e7e-609e-431a-f972-c53fc4bfac10"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing streamlit_app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile streamlit_app.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "st.title(\"🚀 My Colab-to-GitHub Streamlit App\")\n",
        "st.write(\"This app was coded in Google Colab and deployed automatically via GitHub!\")\n",
        "\n",
        "name = st.text_input(\"Enter your name\", \"Developer\")\n",
        "st.success(f\"Hello, {name}!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile requirements.txt\n",
        "streamlit\n",
        "pandas\n",
        "numpy"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jQCsrgUpvfHY",
        "outputId": "dc06dcf6-e865-4628-97b5-8729caa66f1b"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing requirements.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D6nypHGDIRnG",
        "outputId": "7cff1c13-6918-4e14-b24c-822404677a12"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.4/10.4 MB\u001b[0m \u001b[31m119.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.4/11.4 MB\u001b[0m \u001b[31m108.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Start the Streamlit server in the background\n",
        "!streamlit run streamlit_app.py &>/dev/null &\n",
        "\n",
        "# Generate an internal preview link\n",
        "from google.colab import output\n",
        "output.serve_kernel_port_as_iframe(8501)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 421
        },
        "id": "Mp6cwrenIXo-",
        "outputId": "cebbd1b5-7185-468a-b93a-6fb9440515b3"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, width, height, cache, element) => {\n",
              "    if (!google.colab.kernel.accessAllowed && !cache) {\n",
              "      return;\n",
              "    }\n",
              "    element.appendChild(document.createTextNode(''));\n",
              "    const url = await google.colab.kernel.proxyPort(port, {cache});\n",
              "    const iframe = document.createElement('iframe');\n",
              "    iframe.src = new URL(path, url).toString();\n",
              "    iframe.height = height;\n",
              "    iframe.width = width;\n",
              "    iframe.style.border = 0;\n",
              "    iframe.allow = [\n",
              "        'accelerometer',\n",
              "        'autoplay',\n",
              "        'camera',\n",
              "        'clipboard-read',\n",
              "        'clipboard-write',\n",
              "        'gyroscope',\n",
              "        'magnetometer',\n",
              "        'microphone',\n",
              "        'serial',\n",
              "        'usb',\n",
              "        'xr-spatial-tracking',\n",
              "    ].join('; ');\n",
              "    element.appendChild(iframe);\n",
              "  })(8501, \"/\", \"100%\", \"400\", false, window.element)"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}
