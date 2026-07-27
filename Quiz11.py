{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKaoN6K91I/FF6MGXSYKE9",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sarony-2002/streamlit-workshop-template/blob/main/Quiz11.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
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
        "%%writefile quiz2.py\n",
        "import streamlit as st\n",
        "\n",
        "# Page configuration\n",
        "st.set_page_config(page_title=\"Interactive Quiz\", page_icon=\"💡\", layout=\"centered\")\n",
        "\n",
        "st.title(\"💡 Quick Interactive Knowledge Check\")\n",
        "st.write(\"Answer the questions below to test your knowledge! Case-insensitive.\")\n",
        "\n",
        "# Initialize score counter\n",
        "score = 0\n",
        "\n",
        "st.write(\"---\")\n",
        "\n",
        "# ==================== QUESTION 1 ====================\n",
        "st.subheader(\"Question 1\")\n",
        "q1_input = st.text_input(\n",
        "    \"What Python framework allows you to build web applications without needing HTML or CSS?\",\n",
        "    key=\"q1\"\n",
        ")\n",
        "\n",
        "# Process Question 1\n",
        "if q1_input:\n",
        "    # .strip().lower() ignores accidental spaces and capital letters\n",
        "    if q1_input.strip().lower() == \"streamlit\":\n",
        "        st.success(\"✅ Correct! Excellent job.\")\n",
        "        score += 1\n",
        "    else:\n",
        "        st.error(\"❌ Not quite. Try again!\")\n",
        "\n",
        "st.write(\"---\")\n",
        "\n",
        "# ==================== QUESTION 2 ====================\n",
        "st.subheader(\"Question 2\")\n",
        "q2_input = st.text_input(\n",
        "    \"Which platform hosts git repositories and lets you launch cloud-based Codespaces?\",\n",
        "    key=\"q2\"\n",
        ")\n",
        "\n",
        "# Process Question 2\n",
        "if q2_input:\n",
        "    if q2_input.strip().lower() == \"github\":\n",
        "        st.success(\"✅ Correct! Spot on.\")\n",
        "        score += 1\n",
        "    else:\n",
        "        st.error(\"❌ Keep trying!\")\n",
        "\n",
        "st.write(\"---\")\n",
        "\n",
        "# ==================== SCORE BOARD ====================\n",
        "if q1_input or q2_input:\n",
        "    st.markdown(f\"### 📊 Your Current Score: **{score} / 2**\")\n",
        "\n",
        "    # Trigger celebration if all answers are correct\n",
        "    if score == 2:\n",
        "        st.balloons()\n",
        "        st.info(\"🎉 Perfect Score! You've mastered this topic.\")"
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