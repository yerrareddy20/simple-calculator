{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXctJvbjyGS+NBjjHAUuyo",
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
        "<a href=\"https://colab.research.google.com/github/yerrareddy20/simple-calculator/blob/main/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uW1ennuGBXpx",
        "outputId": "caf64197-34ee-4aed-e2cd-60b9d9865fa4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to Simple Calculator\n",
            "Enter first number: 12\n",
            "Enter operator (+, -, *, /): *\n",
            "Enter second number: 6\n",
            "Result: 72.0\n"
          ]
        }
      ],
      "source": [
        "print(\"Welcome to Simple Calculator\")\n",
        "\n",
        "num1 = float(input(\"Enter first number: \"))\n",
        "operator = input(\"Enter operator (+, -, *, /): \")\n",
        "num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "if operator == '+':\n",
        "    print(\"Result:\", num1 + num2)\n",
        "elif operator == '-':\n",
        "    print(\"Result:\", num1 - num2)\n",
        "elif operator == '*':\n",
        "    print(\"Result:\", num1 * num2)\n",
        "elif operator == '/':\n",
        "    if num2 == 0:\n",
        "        print(\"Error! Division by zero.\")\n",
        "    else:\n",
        "        print(\"Result:\", num1 / num2)\n",
        "else:\n",
        "    print(\"Invalid operator.\")"
      ]
    }
  ]
}