import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie #pip
import requests #pip 
import pandas as pd
import boto3
from sqlalchemy import create_engine
import json
import emoji
import numpy as np
import sklearn #pip
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

#Connecting VS-CODE to mysql
# myconnection=pymysql.connect(host='localhost',user='root',passwd='root',port=3306)
# mycursor=myconnection.cursor()

# queary=f'''select topic,profile,channel_Name,video_id,video_name,views,likes,thumbnail,tags from data'''
# mycursor.execute("use final")
# mycursor.execute(queary)
# myconnection.commit()
# fetch2=mycursor.fetchall()
# df_data=pd.DataFrame(fetch2,columns=['topic','profile','channel_Name','video_id','video_name','views','likes','thumbnail','tags'])


# Pull the data from RDS
import boto3
from sqlalchemy import create_engine
import pymysql
db_user = 'admin'
db_password = 'Chusanth0410'
db_host = 'database-1.cheo2e64wg9v.ap-south-1.rds.amazonaws.com' 
db_port = '3306'
db_name = 'youtube'
# print('Connection started...')
connection_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string)
# print('Connection made...')
query = "SELECT * FROM data_df"
df_data = pd.read_sql(query, engine)
# print('Preprocessed data loaded sucessfully')

tags=[]
for i in df_data['tags']:
    tags.append(i)

video_ids=[]
for i in df_data['video_id']:
    video_ids.append(i)

def recommend(user_input):
    # Initialize a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit and transform the animal descriptions
    tfidf_matrix = tfidf_vectorizer.fit_transform(tags)
    # Transform the user input using the same vectorizer
    query_vector = tfidf_vectorizer.transform([user_input])

    # Calculate the cosine similarity between the input query and animal descriptions
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()

    # Sort the animals by similarity (in descending order)
    related_ids_indices = np.argsort(cosine_similarities)[::-1]

    # Get the top 5 recommendations
    top_n = 10
    recommended_ids = [video_ids[i] for i in related_ids_indices][:top_n]
    return recommended_ids

def display_labels(thumbnail,views,likes,title,channel_name,profile,v_id):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(thumbnail,width=200)
    with col2:
        st.write(f"**{title}**")
        a, b = st.columns([1, 2])
        with a:
            st.write(f"Views: :green[{views}]")
        with b:
            st.write(f" :red[{likes}]❤️")
        c,d=st.columns([1,2])
        with c:
            st.image(profile,width=40)
        with d:
            st.write(f":green[**{channel_name}**]")
        with st.expander("Watch Video"):
            st.video(f'https://www.youtube.com/embed/{v_id}')

def display_videos(df):
    for ids in df.index:
            thumbnail=df['thumbnail'][ids]
            views=df['views'][ids]	
            likes=df['likes'][ids]
            title=df['video_name'][ids]
            channel_name=df['channel_Name'][ids]
            profile=df['profile'][ids]
            v_id=df['video_id'][ids]
            display_labels(thumbnail,views,likes,title,channel_name,profile,v_id)
def display_searched_videos(video_ids):
    for ids in video_ids:
        thumbnail=list(df_data[df_data['video_id']==ids].thumbnail)[0]
        views=list(df_data[df_data['video_id']==ids].views)[0]
        likes=list(df_data[df_data['video_id']==ids].likes)[0]
        title=list(df_data[df_data['video_id']==ids].video_name)[0]
        channel_name=list(df_data[df_data['video_id']==ids].channel_Name)[0]
        profile=list(df_data[df_data['video_id']==ids].profile)[0]
        display_labels(thumbnail,views,likes,title,channel_name,profile,ids)

#streamlit part 
with st.sidebar:
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <h1>
        <i class="fab fa-youtube" style="color:red;"></i> YOUTUBE   
    </h1>
    """, unsafe_allow_html=True)
    selected=option_menu(   
    menu_title="Explore",
    options=['Home','Trending','Music','News'],
    menu_icon=["menu-button-wide"],
    icons=["house-gear-fill","fire",'file-earmark-music-fill','newspaper'],
    default_index=0)

if selected=='Home':
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <h2>
        <i class="fab fa-youtube" style="color:red;"></i> YouTube Video Recommendation System
    </h2>
    """, unsafe_allow_html=True)
    user_text = st.text_input('',placeholder="Search")
    if user_text:
        v_ids=recommend(user_text)
        display_searched_videos(v_ids)
        # for ids in v_ids:
        #     st.video(f'https://www.youtube.com/embed/{ids}')
    else:
        df_sorted = df_data.sort_values(by='views',ascending=False).head(50)
        display_videos(df_sorted)       
if selected=='Trending':
    con1, con2 = st.columns([1, 2])
    with con1:
        st.markdown(""" # :red[🔥Trending]""")
    with con2:      
        user_text = st.text_input('',placeholder="Search")

    df_trending = df_data.sort_values(by='likes',ascending=False).head(50)
    display_videos(df_trending)    

if selected=='Music':
    con1, con2 = st.columns([1, 2])
    with con1:
        st.markdown(""" # :blue[🎼Musics]""")
    with con2:      
        user_text = st.text_input('',placeholder="Search")

    df_music = df_data[df_data['topic']=='musics'].sort_values(by='likes',ascending=False).head(50)
    display_videos(df_music) 
if selected=='News':
    con1, con2 = st.columns([1, 2])
    with con1:
        st.markdown(""" # :White[📰News]""")
    with con2:      
        user_text = st.text_input('',placeholder="Search")
    
    df_news = df_data[df_data['topic']=='news'].sort_values(by='likes',ascending=False).head(50)
    display_videos(df_news)              