{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c751a675",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import matplotlib.pylot as plt\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "import json\n",
    "\n",
    "st.title(\"Group_2_assignment3\")\n",
    "\n",
    "#Fetch tweets related to \"Haribo\" using a command:\n",
    "#snscrape --jsonl --progress --max-results 500 --since 2022-10-01 twitter-seach \"#haribo until:2022-10-31\" >haribo.json\n",
    "\n",
    "def load_data():\n",
    "    #Read one twitter per line from haribo.json\n",
    "    with open(\"haribo.json\",\"r\") as f:\n",
    "        tweets = f.readlines()\n",
    "        # Covert json string to dictionary\n",
    "        tweets = [json.loads(tweet) for tweet in tweets]\n",
    "        return tweets\n",
    "    \n",
    "tweets = load_data()\n",
    "# Map json keys to dictionary keys\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
