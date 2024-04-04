import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="ML Jobs Insights",
				   layout="wide")

content_to_hide = """
	<style>
		.st-emotion-cache-18ni7ap { display: none; }
	</style>
"""

st.markdown(content_to_hide, unsafe_allow_html=True)

st.title("Insights from 1000 ML job listings scraped from Linkedin")

libraries_frameworks_dict = { 'Apache Spark': 372, 'Data Visualization': 320, 
							  'Big Data': 239, 'Tensorflow': 149, 'Pytorch': 125, 
							  'Pandas': 116, 'Numpy': 109, 'Scikit-Learn': 105, 
							  'Docker': 99, 'Kubernetes': 86, 'Matplotlib': 29 }

analytics_visualization_dict = { 'tableau': 226, 'SAS': 217, 'Matlab': 62 }

ml_algorithms_dict = { 'NLP': 197, 'Computer Vision': 110 , 'Recommender Systems': 28 }

cloud_platforms_dict = { 'AWS': 595, 'Azure': 472, 'GCP': 101 }

experience_dict = { "1 YoE": 24, "2 YoE": 31, '3 YoE': 58, '4 YoE': 16, '5 YoE': 65 }

education_dict = { 'Computer Science': 665, 'Math': 508, 'Problem Solving': 207 }

data_language_dict = { 'SQL': 1154, 'NoSQL': 94 }

analytics_storage_dict = { 'Data Warehouse/Lake': 438, 'Snowflake': 106, 'Databricks': 101 }


education_df = pd.DataFrame.from_dict(data=education_dict,
                                      orient='index',
                                      columns=['Number of Appearances'])

experience_df = pd.DataFrame.from_dict(data=experience_dict,
									   orient='index',
									   columns=['Number of Appearances'])

ml_algorithms_df = pd.DataFrame.from_dict(data=ml_algorithms_dict,
                                       	  orient='index',
                                       	  columns=['Number of Appearances'])

data_languages_df = pd.DataFrame.from_dict(data=data_language_dict,
                                      	   orient='index',
                                      	   columns=["Number of Appearances"])

analytics_platforms_df = pd.DataFrame.from_dict(data=analytics_storage_dict,
                                      		    orient='index',
                                      		    columns=["Number of Appearances"])

libraries_frameworks_df = pd.DataFrame.from_dict(data=libraries_frameworks_dict,
                                      		orient='index',
                                      		columns=["Number of Appearances"])

cloud_platforms_df = pd.DataFrame.from_dict(data=cloud_platforms_dict,
                                  			orient='index',
                                  			columns=["Number of Appearances"])

job_skills = ["Education & Experience", 
			  "Libaries & Frameworks",
			  "ML Algorithms & Cloud Platforms",
			  "Data Languages & Analytics Platforms",
			]


education_experience, libaries_frameworks, ml_algorithms_cloud_platforms, data_languages_analytics_platforms = st.tabs(job_skills)

with education_experience:

	education_column, experience_column = st.columns(2)

	with education_column:

		figure_education = px.bar(
			education_df,
			x=education_df.index,
			y="Number of Appearances",
			hover_data=[education_df.index, "Number of Appearances"],
			color="Number of Appearances",
			color_continuous_scale="Turbo",
			title="Education",
			width=600
		)

		figure_education.update_layout(bargap=0.6)

		st.plotly_chart(figure_education)

	with experience_column:

		figure_experience = px.bar(
			experience_df,
			x=experience_df.index,
			y="Number of Appearances",
			hover_data=[experience_df.index, "Number of Appearances"],
			color="Number of Appearances",
			color_continuous_scale="Turbo",
			title="Years of Experience",
			width=600
		)

		figure_experience.update_layout(bargap=0.4)

		st.plotly_chart(figure_experience)


with libaries_frameworks:

	figure_experience = px.bar(
		libraries_frameworks_df,
		x=libraries_frameworks_df.index,
		y="Number of Appearances",
		hover_data=[libraries_frameworks_df.index, "Number of Appearances"],
		color="Number of Appearances",
		color_continuous_scale="Bluered_r",
		title="Popular Libraries & Frameworks",
		width=1200,
	)

	figure_experience.update_layout(bargap=0.4)

	st.plotly_chart(figure_experience)


with ml_algorithms_cloud_platforms:

	ml_algorithms_column, cloud_platforms_column = st.columns(2)

	with ml_algorithms_column:

		figure_ml_algorithms = px.bar(
			ml_algorithms_df,
			x=ml_algorithms_df.index,
			y="Number of Appearances",
			hover_data=[ml_algorithms_df.index, "Number of Appearances"],
			color="Number of Appearances",
			color_continuous_scale="Sunset",
			title="Most Popular Class of ML Algorithms",
			width=600
		)

		figure_ml_algorithms.update_layout(bargap=0.6)

		st.plotly_chart(figure_ml_algorithms)


	with cloud_platforms_column:

		figure_cloud_platforms = px.bar(
			cloud_platforms_df,
			x=cloud_platforms_df.index,
			y="Number of Appearances",
			hover_data=[cloud_platforms_df.index, "Number of Appearances"],
			color="Number of Appearances",
			color_continuous_scale="Sunset",
			title="Most Popular Cloud Platforms",
			width=600
		)

		figure_cloud_platforms.update_layout(bargap=0.6)

		st.plotly_chart(figure_cloud_platforms)


with data_languages_analytics_platforms:

	data_languages_column, analytics_platforms_column = st.columns(2)

	with data_languages_column:

		figure_data_languages = px.bar(
			data_languages_df,
			x=data_languages_df.index,
			y="Number of Appearances",
			hover_data=[data_languages_df.index, "Number of Appearances"],
			color="Number of Appearances",
			color_continuous_scale="Tealgrn",
			title="Most Popular Data Programming Languages",
			width=600
		)

		figure_data_languages.update_layout(bargap=0.7)

		st.plotly_chart(figure_data_languages)

	with analytics_platforms_column:

		figure_analytics_platforms = px.bar(
			analytics_platforms_df,
			x=analytics_platforms_df.index,
			y="Number of Appearances",
			hover_data=[analytics_platforms_df.index, "Number of Appearances"],
			color="Number of Appearances",
			color_continuous_scale="Tealgrn",
			title="Most Popular Data Analytics Platforms",
			width=600
		)

		figure_analytics_platforms.update_layout(bargap=0.6)

		st.plotly_chart(figure_analytics_platforms)