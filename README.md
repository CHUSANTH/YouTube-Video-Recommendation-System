# YouTube-Video-Recommendation-System
**Introduction:**
"YouTube-Video-Recommendation-System" initiative aims to Develop a system that collects YouTube channel and video data, group videos based on meta information tags, and provides video recommendations through a Streamlit web application

**Key Technologies:**
1. Python Scripting
2. Google API
3. SQL
4. Streamlit
5. Data Collection
6. Cosine Similarity/ML
7. AWS S3,RDS and EC2 Services

**Install Required Libraries:**

      pip install google-api-python-client
      pip install pymysql
      pip install datatime
      pip install pandas
      pip install isodate
      pip install streamlit
      pip install streamlit-option-menu
      pip install numpy 
      pip install sklearn
      pip install boto3

**Key Features of the Project:**

1. **User-Friendly Interface:**
   - Intuitive Streamlit application with an easy-to-use interface for seamless user interaction.

2. **YouTube Channel Data Retrieval:**
   - Capability to input YouTube channel ID and retrieve comprehensive data (name, subscribers, video count, etc.) using the Google API.

3. **Batch Data Collection:**
   - Ability to collect data for up to 10 different YouTube channels simultaneously, enhancing efficiency.

4. **SQL Data Warehouse Migration:**
   - Option to migrate collected data from api to a SQL data warehouse (MySQL) for structured organization.

5. **SQL Database Search and Retrieval:**
   - Advanced search options within the SQL database, including the ability to join tables for comprehensive data retrieval.

6. **Data Visualization with Streamlit:**
   - Utilization of Streamlit's features for effective data visualization, enhancing user understanding of the collected information.

7. **API Integration:**
   - Seamless integration with the Google API for retrieving real-time and accurate YouTube channel data.

8. **Dynamic Data Analysis:**
   - Dynamic analysis and exploration of YouTube channel data within the Streamlit app, facilitating insights generation.
   - 
9. **Python Scripting for Automation:**
    - Utilization of Python scripting for automation of data collection, migration, and other essential tasks.

10. **User-Driven Data Exploration:**
    - Empowering users to search, retrieve, and explore data based on specific criteria, enhancing user autonomy.
11. **Pertinent Recommendation system**
    - Recommended videos are more correlated to the user input

**In-Depth Analytics: Channel & Video Analysis, Model Building and Model Hosting**

**Channel Analysis:**
Channel analysis provides detailed insights into playlists, videos, subscribers, views, likes, comments, and durations. Develop a profound understanding of the channel's performance and audience engagement through comprehensive visualizations and insightful summaries.

**Video Analysis:**
Video analysis hones in on views, likes, comments, and durations, offering perspectives from both an overall channel and specific video standpoint. Harness visual representations and metrics to glean valuable insights, enhancing the understanding of individual video performance. Dive deeper into the analytics to uncover nuanced details and trends that contribute to informed decision-making.

**Model Building**
The heart of the YouTube Video Recommendation System lies in its ability to provide personalized and relevant video recommendations. The model building phase utilizes Cosine Similarity to measure the similarity between video meta information using tags attribute.

**Model Hosting**
EC2 provides a scalable cloud computing environment where the model can handle real-time inference requests. EC2 instances are chosen based on the computational needs of the model, ensuring it can process large amounts of data and provide quick recommendations.

**Streamlit Overview: Crafting User-Friendly Recommendation System**
Create dynamic and interactive Recommendation System effortlessly with Streamlit, a powerful Python library. Streamlit simplifies the process of transforming data scripts into shareable web apps, requiring minimal code. Design visually appealing dashboards, charts, and interfaces to present and Recommend your data seamlessly. Whether you're a data scientist or developer, Streamlit offers an intuitive way to showcase your Recommendation System in a user-friendly environment.

**Conclusion:**

This project successfully delivers a Streamlit-based tool for Recommending videos, integrating AWS S3 and RDS for data storage and structured querying. With Python scripting and API integration, users can effortlessly explore and manage data from multiple channels. The project provides valuable skills in data collection, management, visualization, deploying model, offering a versatile Recommendation System
for Youtube.
