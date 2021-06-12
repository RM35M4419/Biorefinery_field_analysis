# Biorefinery_field_analysis
Analysis of tweets containing biorefinery keywords

## 1. Biorefinery Twits analysis with Topic Modeling

## Objective
1. Make a general analysis with descriptive statistics of the Tweets that include the keyword "Biorefinery".
2. Understand the use of sklearn and LDAvis libraries with actual useful data, and my own code.
3. Compose a database from the scraped content for future use.

## Algorithm
1. DATA PREPARATION
 - Import & combine tweets json into a DF
 - Clean up tweets DF (remove useless fields)
 - Import & combine user json into a DF
 - Clean up users DF (remove useless fields)
 - Combine both DFs by user_id
 - Export final DF to disk for future use
2. DESCRIPTIVE STATISTICS
 - Note: see [[20210405082339]]
 + Oldest tweet
 + Oldest tweet in relation to the network age
 + Proportions of discussions / retweets with sole tweets / unfavorited
 + Growth of the subject level of discussion, in relation to the growth of the network usage
 + Are there clusters of frequent interacting actors? 
     + Is it possible to link it with _real-world_ links? (associations, contracts, commercial relations)
 + What is noise in a tweeter feed? Has it been defined, measured, operationalized?
 + Proportion of personal and organization accounts
3. LDA ANALYSIS
 - Single tweet as document
 - Tweets for each month/year as document
 - Tweets for each user as document
4. RQ LINKED TO INSTITUTIONAL THEORY
 + Are evident logics  in the top 50/100 favorited or retweeted texts?
 + Is it possible to trace diffusion of logics?
 + Is there evidence of Institutional Infrastructure in the tweets?
 + Can we identify actors (users in normative and coercive positions?
 + What is the best way to segment the users, based on IT?
 + Is it possible to identify explicit proposed practices?
     + If so, are they promoted as efficient or legitimate? Or both?
 + Is it possible to identify lobbing streams? 
     + Would this help map institutional work?
