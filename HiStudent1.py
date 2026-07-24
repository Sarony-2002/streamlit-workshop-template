{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "V5E1",
      "authorship_tag": "ABX9TyNk9wl4pKazlXzks0X3EBn1"
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
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sDpUJ2-UnjKe",
        "outputId": "3ba3db4b-d7e5-497d-9df6-791feed95bb1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile HiStudent.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "st.title(\"🚀 My First Streamlit App\")\n",
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