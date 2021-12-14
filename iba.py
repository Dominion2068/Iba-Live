import pandas as pd  
import numpy as np
import plotly.express as px  
import streamlit as st 
import plotly.graph_objects as go

st.set_page_config(page_title="Iba Live Dashboard", 
page_icon=":pie chart:", layout="wide")

#st.header('Visuals For Iba Live Facebook Programme')

# Load DataFrame
dataset = pd.read_csv("data.csv")
#st.subheader('Full Dataset')
#st.write(dataset)

# upload_file = st.file_uploader('Choose a file')
# if upload_file is not None:
#     dataset = pd.read_csv(upload_file)
#     st.write(dataset)

# side bar
st.sidebar.header('Filter Data Here')
month = st.sidebar.multiselect(
    'Select Months: you can select one, some or all the months. By default, all the months are selected',
    options=dataset['Month_Name'].unique(),
    default=dataset['Month_Name'].unique()
)
st.sidebar.markdown("""----""")
# gender = st.sidebar.multiselect(
#     'Select Gender Male or Female:',
#     options=dataset['Gender'].unique(),
#     default=dataset['Gender'].unique()
# )
# date = st.sidebar.multiselect(
#     'Select Date:',
#     options=dataset['Date'].unique(),
#     default=dataset['Date'].unique()
# )
dataset_selection = dataset.query(
    'Month_Name == @month'
)
# st.subheader('Filtered Data')
# st.write(dataset_selection)
#length = (len(dataset_selection()))
#st.(length)
#st.write(dataset_selection.shape)
# st.write('Rows of Filtered Data=',(dataset_selection.shape[0]),
# 'Columns=',(dataset_selection.shape[1]))

# ---- MAINPAGE ----
#st.title(":bar_chart: Sales Dashboard")
st.title(":bar_chart:  Iba Live Facebook Show")
#st.subheader("Powered by XYZ Bank")
#st.markdown("##")

# Top KPIs
participants_total = len(dataset_selection)
state_count = dataset_selection['State'].nunique()
country_count = dataset_selection['Country'].nunique()
average_rating = round(dataset_selection["Ratings"].mean(), 1)
active = dataset_selection[(dataset_selection['Participation_Status']=='Active')]
star_rating = ":star:" * int(round(average_rating, 0))

left_column, middle_column, right_column, beta_column,beta1_column = st.columns(5)
with left_column:
    st.markdown("**Total Participants:**")
    st.markdown(f" **{participants_total:,}**")
with beta1_column:
    st.markdown("**Active Participants:**")
    st.markdown(f"**{len(active)}**")
with middle_column:
    st.markdown("**Average Rating:**")
    st.markdown(f"**{average_rating} {star_rating}**")
with right_column:
    st.markdown("**Total States:**")
    st.markdown(f"**{state_count}**")
with beta_column:
    st.markdown("**Total Countries:**")
    st.markdown(f"**{country_count}**")
st.markdown("""---""")
st.markdown("- *Active participants are those who contributed one way or another to a particular episode before, during or after through their comments, enquiries, facilitation etc. The passive participants attended the online show but made no comments*")
st.markdown('- *Hover on the graphs to interact with them*')
st.markdown('- *Use any of the icons above each graph accordingly. However, we recommend that you click on the last icon to your right to compare data on hover most especially for the line charts*')
st.markdown('- *The sidebar scroll differently from the main page. Filter by months to see changes on the main page*')
st.markdown('- *To check the events in the community, scroll on the sidebar*')
st.markdown("""---""")


data1 = dataset_selection.groupby(['Month_Name','Gender'])['Counter'].count().reset_index().sort_values('Counter',ascending=False)
#data1

fig1 = px.bar(data1,
y ='Counter',
x ='Month_Name',
color ='Gender',
width=455, 
height=500,
#orientation = 'h',
      title='Participants by Gender Distribution',
        #color_discrete_sequence=["#0083B8"] * len(data1),
    template="plotly_white",
    color_discrete_sequence=['gray',
                           'royalblue'])
#st.write(fig1)
#st.plotly_chart(fig)

#fig = go.Figure()
fig2 = px.bar(data1, x ='Month_Name',
             y='Counter',
             color='Gender',
             opacity=0.9,
             #orientation='h',
             barmode='relative')
#st.plotly_chart(fig)
#st.write(fig2)

# data2 = dataset_selection.groupby(['Title'])['Counter'].count().reset_index()
# data2

fig3 = px.pie(data1, values ='Counter',
names='Gender',
width=500, 
#height=500,
      #title='Gender Distribution Pie Chart',
        color_discrete_map=['lightcyan',
                           'royalblue'])
#st.write(fig3)
left_column, right_column = st.columns(2)

with left_column:
    #st.markdown("**Gender Distribution Bar Chart**")
    st.write(fig1)

with right_column:
    #st.markdown("**Gender Distribution Pie Chart**")
    st.write(fig3)
    
data3 = dataset_selection.groupby(['Month_Name','Title','Gender'])['Counter'].count().reset_index().sort_values('Counter',ascending=False)
#data3
#fig = go.Figure()
fig4 = px.bar(data3, x ='Title',
             y='Counter',
             color='Gender',
             opacity=0.9,
             orientation='v',
             title = 'Gender Composition of Participants by Titles per Month',
             barmode='relative',
            facet_col='Month_Name',
            facet_col_wrap=2,
            width=900, 
            height=600,
            color_discrete_sequence=['green',
                           'purple'])
st.write(fig4)

data4 = dataset_selection.groupby(['Month_Name','Title','Participation_Status'])['Counter'].count().reset_index().sort_values('Counter',ascending=False)
#data4

#fig = go.Figure()
fig5 = px.bar(data4, x ='Title',
             y='Counter',
             color='Participation_Status',
             opacity=0.9,
             orientation='v',
             title = 'Participatory Status of Participants by Titles per Month',
             barmode='relative',
            facet_col='Month_Name',
            facet_col_wrap=2,
            width=900, 
            height=600,
            color_discrete_sequence=['darkcyan',
                           'purple'])
st.write(fig5)

data7 = dataset_selection.groupby(['Episode','Gender'])['Counter'].count().reset_index().sort_values('Counter',ascending=False)
#data7
fig8 = px.bar(data7,
y ='Counter',
x ='Episode',
color ='Gender',
width=900, 
height=600,
#orientation = 'h',
      title='Paticipants Gender Composition Per Episode',
        #color_discrete_sequence=["#0083B8"] * len(data1),
    template="plotly_white",
    color_discrete_sequence=['blue',
                           'sandybrown'])
st.write(fig8)         

data8 = dataset_selection.groupby(['Episode','Title'])['Counter'].count().reset_index().sort_values('Counter',ascending=False)
#data8

fig9 = px.bar(data8,
y ='Counter',
x ='Episode',
color ='Title',
width=900, 
height=600,
#orientation = 'h',
      title='Participants Title Composition Per Episode',
        #color_discrete_sequence=["#0083B8"] * len(data1),
    template="plotly_white",
    color_discrete_sequence=['mediumaquamarine','oldlace',
                           'sandybrown'])
st.write(fig9)

data5 = dataset_selection.groupby(['Date','Gender'])['Counter'].count().reset_index()
#data5

fig6 = px.line(data5, x='Date', y='Counter', color='Gender',
    title = 'Movements of Participants by Gender Per Date',
    width=900, 
            height=600,
    color_discrete_sequence=['pink',
                           'darkblue'])
st.write(fig6)

data6 = dataset_selection.groupby(['Date','Title'])['Counter'].count().reset_index()
#data6

fig7 = px.line(data6, x='Date', y='Counter', color='Title',
    title = 'Movements of Participants by Titles Per Date',
    width=900, 
            height=600,
    color_discrete_sequence=[
                           'darkolivegreen', 'turquoise', 'khaki'])

st.write(fig7)

# from PIL import Image
# img = Image.open('img1.jpg')
# st.image(img,width=100,caption='POTM Female')

st.sidebar.write('**Community: Current Storyline in Pictures**')
col1, col2 = st.sidebar.columns(2)

col1.image('img1.jpg',width=150,caption='POTM Female')
col2.image('img2.jpg',width=150,caption='POTM Male')

col1.image('img5.jpg',width=150,caption='Happy Birthday Buka')
col2.markdown('*Thank you for your service to the community we appreciate you; cheers to a new age*')

col1, col2 = st.sidebar.columns(2)
col1.image('img6.jpg',width=150,caption='The Enigma')
col2.markdown('*We always look up to you, and you never fail to deliver. You are blessed beyond measures. Thank you!*')

col1, col2 = st.sidebar.columns(2)
col1.image('img8.jpg',width=150,caption='Thumbs up Otunba')
col2.markdown('*Congratulations on your recent appointment. We wish you the very best*')

col1, col2 = st.sidebar.columns(2)
col1.image('img9.jpg',width=150,caption='Thumbs up Otunba')
col2.markdown('*Your mentees say thank you and we say thank you for providing a platform for our youths to grow*')

col1, col2 = st.sidebar.columns(2)
col1.image('img3.jpg',width=150,caption='Sassy Katie')
col2.markdown('*Beauty and Brains*')


st.sidebar.image('img7.jpg',width=300,caption='Family Love: without our families we are nothing')
#st.sidebar.markdown("*QOTM: Coincidence is God's way of remaining anonymous* - Albert Einstein")
st.sidebar.markdown("""---""")
# st.sidebar.image('img10.jpg',width=150)#,caption='Automate your invites, and reach more people')
# st.sidebar.markdown('[Automate your invites](https://www.facebook.com/EInvites-App-104982628594021/)')
# st.sidebar.image('img11.jpg',width=150)
# st.sidebar.markdown('[December Clearance Sales](https://www.facebook.com/corneressence/)')

col1, col2 = st.sidebar.columns(2)

col1.image('img10.jpg',width=100)
col1.markdown('[Automate your invites](https://www.facebook.com/EInvites-App-104982628594021/)')

col2.image('img11.jpg',width=100)
col2.markdown('[December Clearance Sales](https://www.facebook.com/corneressence/)')


data9 = dataset_selection.groupby(['Country','Country_Abb'])['Counter'].count().reset_index()
data9['Counter'] = data9['Counter'].astype(np.float)
#data9
fig10 = px.choropleth(data9,
                    locations='Country_Abb',
                    color = 'Counter',
                    hover_name='Country',
                    projection ='natural earth',
                    width=800, 
                    height=600,
                    title = 'Participants by Country of Residence',
                    color_continuous_scale=px.colors.sequential.Plasma)
#st.plotly_chart(fig10)
st.write(fig10)

#st.markdown("*To Enjoy More Interactivity, kindlt clicl on the last icon on the far right on each graph*")
data10 = dataset_selection.groupby(['State','Gender'])['Counter'].count().reset_index()
#data10
fig11 = scatterplot = px.scatter(
        data_frame=data10,
        x = 'State',
        y = 'Counter',
        color ='Gender',
        hover_data=['State'],
        text = 'State',
        height = 550,
        width=800,
        title = 'Geographical Spread of Participants by Gender'
    )
scatterplot.update_traces(textposition='top center')
st.markdown("*To enjoy more interactivity, click on the icon before the plotly logo far right on each graph*")
st.write(fig11)

data11 = dataset_selection.groupby(['State','Title'])['Counter'].count().reset_index()
#data11
fig12 = scatterplot = px.scatter(
        data_frame=data11,
        x = 'State',
        y = 'Counter',
        color ='Title',
        hover_data=['State'],
        text = 'State',
        height = 700,
        width = 900,
        title = 'Geographical Spread of Participants by Title',
        
    )
scatterplot.update_traces(textposition='top center')

st.write(fig12)


data12 = dataset_selection.groupby(['State','Episode'])['Counter'].count().reset_index()
#data12
fig13 = scatterplot = px.scatter(
        data_frame=data12,
        x = 'State',
        y = 'Counter',
        color ='Episode',
        hover_data=['State'],
        #text = 'State',
        height = 700,
        width = 800,
        title = 'Geographical Spread of Participants by Episodes',
        
    )
scatterplot.update_traces(textposition='top center')

st.write(fig13)

