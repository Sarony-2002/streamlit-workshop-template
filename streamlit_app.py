{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyPaBpS7aOFGobnoCA2mS5Jp",
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sarony-2002/streamlit-workshop-template/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "outputId": "92487b37-455f-4158-d7ed-0212bc4c79d3"
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
        "outputId": "577944e2-22c3-4c75-ea63-8cfc33dab240"
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
    }
  ]
}
