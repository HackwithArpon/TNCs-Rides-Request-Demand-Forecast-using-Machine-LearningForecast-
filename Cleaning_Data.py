{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Data Cleaning (Basic).ipynb\r\n",
      "2. Data Analysis and Cleaning (Advance).ipynb\r\n",
      "3. Data Prep.ipynb\r\n",
      "4. Model_Training.ipynb\r\n",
      "data_analysis_ride_request.html\r\n"
     ]
    }
   ],
   "source": [
    "!ls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Reading DataSet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8381556"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('../Data/raw_data.csv', low_memory = False, compression='gzip')\n",
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ts</th>\n",
       "      <th>number</th>\n",
       "      <th>pick_lat</th>\n",
       "      <th>pick_lng</th>\n",
       "      <th>drop_lat</th>\n",
       "      <th>drop_lng</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2020-03-26 07:07:17</td>\n",
       "      <td>14626</td>\n",
       "      <td>12.313621</td>\n",
       "      <td>76.658195</td>\n",
       "      <td>12.287301</td>\n",
       "      <td>76.602280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2020-03-26 07:32:27</td>\n",
       "      <td>85490</td>\n",
       "      <td>12.943947</td>\n",
       "      <td>77.560745</td>\n",
       "      <td>12.954014</td>\n",
       "      <td>77.543770</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-03-26 07:36:44</td>\n",
       "      <td>05408</td>\n",
       "      <td>12.899603</td>\n",
       "      <td>77.587300</td>\n",
       "      <td>12.934780</td>\n",
       "      <td>77.569950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020-03-26 07:38:00</td>\n",
       "      <td>58940</td>\n",
       "      <td>12.918229</td>\n",
       "      <td>77.607544</td>\n",
       "      <td>12.968971</td>\n",
       "      <td>77.636375</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2020-03-26 07:39:29</td>\n",
       "      <td>05408</td>\n",
       "      <td>12.899490</td>\n",
       "      <td>77.587270</td>\n",
       "      <td>12.934780</td>\n",
       "      <td>77.569950</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    ts number   pick_lat   pick_lng   drop_lat   drop_lng\n",
       "0  2020-03-26 07:07:17  14626  12.313621  76.658195  12.287301  76.602280\n",
       "1  2020-03-26 07:32:27  85490  12.943947  77.560745  12.954014  77.543770\n",
       "2  2020-03-26 07:36:44  05408  12.899603  77.587300  12.934780  77.569950\n",
       "3  2020-03-26 07:38:00  58940  12.918229  77.607544  12.968971  77.636375\n",
       "4  2020-03-26 07:39:29  05408  12.899490  77.587270  12.934780  77.569950"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A Customer_ID `number` at a particular timestamp can only have one entry\n",
    "### Removing Duplicate Entries ['ts','number']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ts</th>\n",
       "      <th>number</th>\n",
       "      <th>pick_lat</th>\n",
       "      <th>pick_lng</th>\n",
       "      <th>drop_lat</th>\n",
       "      <th>drop_lng</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>235</th>\n",
       "      <td>2020-03-26 18:10:35</td>\n",
       "      <td>16795</td>\n",
       "      <td>12.967236</td>\n",
       "      <td>77.641594</td>\n",
       "      <td>13.014504</td>\n",
       "      <td>77.650856</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>236</th>\n",
       "      <td>2020-03-26 18:10:35</td>\n",
       "      <td>16795</td>\n",
       "      <td>12.967236</td>\n",
       "      <td>77.641594</td>\n",
       "      <td>13.014504</td>\n",
       "      <td>77.650856</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>407</th>\n",
       "      <td>2020-03-26 21:35:50</td>\n",
       "      <td>65856</td>\n",
       "      <td>12.917173</td>\n",
       "      <td>77.586400</td>\n",
       "      <td>12.913940</td>\n",
       "      <td>77.685280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>408</th>\n",
       "      <td>2020-03-26 21:35:50</td>\n",
       "      <td>65856</td>\n",
       "      <td>12.917173</td>\n",
       "      <td>77.586400</td>\n",
       "      <td>12.913940</td>\n",
       "      <td>77.685280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>443</th>\n",
       "      <td>2020-03-26 23:26:29</td>\n",
       "      <td>27554</td>\n",
       "      <td>12.933715</td>\n",
       "      <td>77.619300</td>\n",
       "      <td>12.938208</td>\n",
       "      <td>77.587520</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8381231</th>\n",
       "      <td>2021-03-26 22:23:12</td>\n",
       "      <td>61636</td>\n",
       "      <td>12.975229</td>\n",
       "      <td>77.620370</td>\n",
       "      <td>13.017285</td>\n",
       "      <td>77.618200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8381245</th>\n",
       "      <td>2021-03-26 22:25:13</td>\n",
       "      <td>61636</td>\n",
       "      <td>12.975229</td>\n",
       "      <td>77.620370</td>\n",
       "      <td>13.017285</td>\n",
       "      <td>77.618200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8381246</th>\n",
       "      <td>2021-03-26 22:25:13</td>\n",
       "      <td>61636</td>\n",
       "      <td>12.975229</td>\n",
       "      <td>77.620370</td>\n",
       "      <td>13.017285</td>\n",
       "      <td>77.618200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8381248</th>\n",
       "      <td>2021-03-26 22:25:27</td>\n",
       "      <td>61636</td>\n",
       "      <td>12.975229</td>\n",
       "      <td>77.620370</td>\n",
       "      <td>13.017285</td>\n",
       "      <td>77.618200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8381249</th>\n",
       "      <td>2021-03-26 22:25:27</td>\n",
       "      <td>61636</td>\n",
       "      <td>12.975229</td>\n",
       "      <td>77.620370</td>\n",
       "      <td>13.017285</td>\n",
       "      <td>77.618200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>113540 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                          ts number   pick_lat   pick_lng   drop_lat  \\\n",
       "235      2020-03-26 18:10:35  16795  12.967236  77.641594  13.014504   \n",
       "236      2020-03-26 18:10:35  16795  12.967236  77.641594  13.014504   \n",
       "407      2020-03-26 21:35:50  65856  12.917173  77.586400  12.913940   \n",
       "408      2020-03-26 21:35:50  65856  12.917173  77.586400  12.913940   \n",
       "443      2020-03-26 23:26:29  27554  12.933715  77.619300  12.938208   \n",
       "...                      ...    ...        ...        ...        ...   \n",
       "8381231  2021-03-26 22:23:12  61636  12.975229  77.620370  13.017285   \n",
       "8381245  2021-03-26 22:25:13  61636  12.975229  77.620370  13.017285   \n",
       "8381246  2021-03-26 22:25:13  61636  12.975229  77.620370  13.017285   \n",
       "8381248  2021-03-26 22:25:27  61636  12.975229  77.620370  13.017285   \n",
       "8381249  2021-03-26 22:25:27  61636  12.975229  77.620370  13.017285   \n",
       "\n",
       "          drop_lng  \n",
       "235      77.650856  \n",
       "236      77.650856  \n",
       "407      77.685280  \n",
       "408      77.685280  \n",
       "443      77.587520  \n",
       "...            ...  \n",
       "8381231  77.618200  \n",
       "8381245  77.618200  \n",
       "8381246  77.618200  \n",
       "8381248  77.618200  \n",
       "8381249  77.618200  \n",
       "\n",
       "[113540 rows x 6 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.duplicated(subset=['ts','number'],keep=False)]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### There are 113540 Duplicate Entries\n",
    "#### We have 8315498 Unique timestamp, customer_id rows. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Keeping first occurence\n",
    "df.drop_duplicates(subset=['ts','number'], inplace = True, keep = 'last')\n",
    "\n",
    "df.reset_index(inplace = True, drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 8315498 entries, 0 to 8315497\n",
      "Data columns (total 6 columns):\n",
      "ts          object\n",
      "number      object\n",
      "pick_lat    float64\n",
      "pick_lng    float64\n",
      "drop_lat    float64\n",
      "drop_lng    float64\n",
      "dtypes: float64(4), object(2)\n",
      "memory usage: 380.7+ MB\n"
     ]
    }
   ],
   "source": [
    "# Info of Dataset\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count missing values\n",
    "np.count_nonzero(df.isnull().values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "116"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['number'] = pd.to_numeric(df['number'], errors = 'coerce')\n",
    "\n",
    "#Count missing values\n",
    "np.count_nonzero(df.isnull().values)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### There are 116 NaN rows, dropping NaN rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8315382"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna(inplace = True)\n",
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['number'] = pd.to_numeric(df['number'], errors = 'coerce', downcast='integer')\n",
    "df['ts'] = pd.to_datetime(df['ts'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 8315382 entries, 0 to 8315497\n",
      "Data columns (total 6 columns):\n",
      "ts          datetime64[ns]\n",
      "number      int32\n",
      "pick_lat    float64\n",
      "pick_lng    float64\n",
      "drop_lat    float64\n",
      "drop_lng    float64\n",
      "dtypes: datetime64[ns](1), float64(4), int32(1)\n",
      "memory usage: 412.4 MB\n"
     ]
    }
   ],
   "source": [
    "# Info of Dataset\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Breaking Time to Features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['hour'] = df['ts'].dt.hour\n",
    "df['mins'] = df['ts'].dt.minute\n",
    "df['day'] = df['ts'].dt.day\n",
    "df['month'] = df['ts'].dt.month\n",
    "df['year'] = df['ts'].dt.year\n",
    "df['dayofweek'] = df['ts'].dt.dayofweek"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('../Data/data_checkpoint/preprocessed_1.csv',index = False, compression = 'gzip')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ts</th>\n",
       "      <th>number</th>\n",
       "      <th>pick_lat</th>\n",
       "      <th>pick_lng</th>\n",
       "      <th>drop_lat</th>\n",
       "      <th>drop_lng</th>\n",
       "      <th>hour</th>\n",
       "      <th>mins</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>dayofweek</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2020-03-26 07:07:17</td>\n",
       "      <td>14626</td>\n",
       "      <td>12.313621</td>\n",
       "      <td>76.658195</td>\n",
       "      <td>12.287301</td>\n",
       "      <td>76.602280</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2020-03-26 07:32:27</td>\n",
       "      <td>85490</td>\n",
       "      <td>12.943947</td>\n",
       "      <td>77.560745</td>\n",
       "      <td>12.954014</td>\n",
       "      <td>77.543770</td>\n",
       "      <td>7</td>\n",
       "      <td>32</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-03-26 07:36:44</td>\n",
       "      <td>5408</td>\n",
       "      <td>12.899603</td>\n",
       "      <td>77.587300</td>\n",
       "      <td>12.934780</td>\n",
       "      <td>77.569950</td>\n",
       "      <td>7</td>\n",
       "      <td>36</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020-03-26 07:38:00</td>\n",
       "      <td>58940</td>\n",
       "      <td>12.918229</td>\n",
       "      <td>77.607544</td>\n",
       "      <td>12.968971</td>\n",
       "      <td>77.636375</td>\n",
       "      <td>7</td>\n",
       "      <td>38</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2020-03-26 07:39:29</td>\n",
       "      <td>5408</td>\n",
       "      <td>12.899490</td>\n",
       "      <td>77.587270</td>\n",
       "      <td>12.934780</td>\n",
       "      <td>77.569950</td>\n",
       "      <td>7</td>\n",
       "      <td>39</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8315493</th>\n",
       "      <td>2021-03-26 23:55:24</td>\n",
       "      <td>50410</td>\n",
       "      <td>12.907856</td>\n",
       "      <td>77.557870</td>\n",
       "      <td>12.954270</td>\n",
       "      <td>77.530785</td>\n",
       "      <td>23</td>\n",
       "      <td>55</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2021</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8315494</th>\n",
       "      <td>2021-03-26 23:58:15</td>\n",
       "      <td>12580</td>\n",
       "      <td>12.981010</td>\n",
       "      <td>77.694450</td>\n",
       "      <td>12.969070</td>\n",
       "      <td>77.704280</td>\n",
       "      <td>23</td>\n",
       "      <td>58</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2021</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8315495</th>\n",
       "      <td>2021-03-26 22:11:20</td>\n",
       "      <td>72339</td>\n",
       "      <td>12.924252</td>\n",
       "      <td>77.650520</td>\n",
       "      <td>12.905820</td>\n",
       "      <td>77.630570</td>\n",
       "      <td>22</td>\n",
       "      <td>11</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2021</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8315496</th>\n",
       "      <td>2021-03-26 22:12:30</td>\n",
       "      <td>72339</td>\n",
       "      <td>12.924252</td>\n",
       "      <td>77.650520</td>\n",
       "      <td>12.905820</td>\n",
       "      <td>77.630570</td>\n",
       "      <td>22</td>\n",
       "      <td>12</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2021</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8315497</th>\n",
       "      <td>2021-03-26 15:00:55</td>\n",
       "      <td>28043</td>\n",
       "      <td>12.901222</td>\n",
       "      <td>77.594890</td>\n",
       "      <td>12.908599</td>\n",
       "      <td>77.649330</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>26</td>\n",
       "      <td>3</td>\n",
       "      <td>2021</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8315382 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                         ts  number   pick_lat   pick_lng   drop_lat  \\\n",
       "0       2020-03-26 07:07:17   14626  12.313621  76.658195  12.287301   \n",
       "1       2020-03-26 07:32:27   85490  12.943947  77.560745  12.954014   \n",
       "2       2020-03-26 07:36:44    5408  12.899603  77.587300  12.934780   \n",
       "3       2020-03-26 07:38:00   58940  12.918229  77.607544  12.968971   \n",
       "4       2020-03-26 07:39:29    5408  12.899490  77.587270  12.934780   \n",
       "...                     ...     ...        ...        ...        ...   \n",
       "8315493 2021-03-26 23:55:24   50410  12.907856  77.557870  12.954270   \n",
       "8315494 2021-03-26 23:58:15   12580  12.981010  77.694450  12.969070   \n",
       "8315495 2021-03-26 22:11:20   72339  12.924252  77.650520  12.905820   \n",
       "8315496 2021-03-26 22:12:30   72339  12.924252  77.650520  12.905820   \n",
       "8315497 2021-03-26 15:00:55   28043  12.901222  77.594890  12.908599   \n",
       "\n",
       "          drop_lng  hour  mins  day  month  year  dayofweek  \n",
       "0        76.602280     7     7   26      3  2020          3  \n",
       "1        77.543770     7    32   26      3  2020          3  \n",
       "2        77.569950     7    36   26      3  2020          3  \n",
       "3        77.636375     7    38   26      3  2020          3  \n",
       "4        77.569950     7    39   26      3  2020          3  \n",
       "...            ...   ...   ...  ...    ...   ...        ...  \n",
       "8315493  77.530785    23    55   26      3  2021          4  \n",
       "8315494  77.704280    23    58   26      3  2021          4  \n",
       "8315495  77.630570    22    11   26      3  2021          4  \n",
       "8315496  77.630570    22    12   26      3  2021          4  \n",
       "8315497  77.649330    15     0   26      3  2021          4  \n",
       "\n",
       "[8315382 rows x 12 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}