{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled",
      "provenance": [],
      "authorship_tag": "ABX9TyPaPJqq2rYyA5U0VZntq7TE"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "M9SE721ffn0B"
      },
      "source": [
        "import yfinance as yf\r\n",
        "import streamlit as st\r\n",
        "\r\n",
        "st.write(\"\"\"\r\n",
        "# Simple Stock Price App\r\n",
        "Shown are the stock closing price and volume of Google!\r\n",
        "\"\"\")\r\n",
        "\r\n",
        "tickerSymbol = 'AMZN'\r\n",
        "\r\n",
        "tickerData = yf.Ticker(tickerSymbol)\r\n",
        "tickerDf = tickerData.history(period='1d', start='2015-12-31', end='2020-12-31')\r\n",
        "\r\n",
        "# Open\tHigh\tLow\tClose\tVolume\tDividends\tStock Splits\r\n",
        "\r\n",
        "st.line_chart(tickerDf.Close)\r\n",
        "st.line_chart(tickerDf.Volume)"
      ],
      "execution_count": 2,
      "outputs": []
    }
  ]
}