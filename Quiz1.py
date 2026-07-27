{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM2bwIp57/yP+o9wLGZ5b2M"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mR4WNcCylF-3",
        "outputId": "9bb513e0-9871-401f-b527-1ad941c39383"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing quiz2.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "\n",
        "st.title(\"🚀 My Quiz App\")\n",
        "st.write(\"Welcome to my clean Streamlit app created in Colab!\")\n",
        "\n",
        "name = st.text_input(\"Enter your name\", \"Developer\")\n",
        "if name:\n",
        "    st.success(f\"Hello, {name}!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "lD-o39Y1q2nU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
