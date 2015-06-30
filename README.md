# Stat Tracker

## Description

Build an application people can use to track any stats they want about themselves on a daily basis.

## Objectives

After completing this assignment, you should be able to:

* Work on a cross-discipline team
* Build an API
* Build a single-page UI using Backbone router (and optionally models, collections, and views)

## Details

### Deliverables

* A Git repo called stat-tracker containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a way to seed your application with data
* An instance of your app running on Heroku

### Requirements  

* No PEP8 or Pyflakes warnings or errors
* Meets API specifications

## Normal Mode

You are going to build an application to track personal statistics about their activities. A personal statistic is a numerical record for a person in a time series by day. For example, let's say I wanted to track how many flights of stairs I walked up in a day. My last week might look like:

Date       | Flights
---------- | -------
06/19/2015 | 8 
06/20/2015 | 6 
06/21/2015 | 7 
06/22/2015 | 6
06/23/2015 | 8
06/24/2015 | 4
06/25/2015 | 6

Users of your application can create as many different activities to track as they want. They should have an easy-to-use interface to track their activities, allowing them to enter the number for the current day or any previous day.

You should allow for:

* User registration
* User login
* Creating a new activity to track
* Recording a stat for an activity for a day
* Editing a stat
* Showing a chart for an activity for any series of dates, defined by a start and stop date. The default should be the last 30 days.

Your chart will be done with D3. We'll learn about this on Tuesday, so you will not have to build it until then.

Your application will be made up of an API and a JavaScript single-page app.

### API Specification

For your API, I'm specifying the endpoints you'll need and what they should do. The URLs I'm using are not prefixed: yours should have `/api/` in front of them.

All the endpoints require authentication.

Verb   | URL  | Action
------ | ---- | -------
GET | /activities | Show a list of all activities I am tracking, and links to their individual pages
POST | /activities | Create a new activity for me to track.
GET | /activities/{id} | Show information about one activity I am tracking, and give me the data I have recorded for that activity.
PUT | /activities/{id} | Update one activity I am tracking, changing attributes such as name or type. Does not allow for changing tracked data.
DELETE | /activities/{id} | Delete one activity I am tracking. This should remove tracked data for that activity as well.
GET | /activities/{id}/stats | Get tracked data for an activity. Paginated.
POST | /activities/{id}/stats | Add tracked data for a day. The data sent with this should include the day tracked.
PUT | /stats/{id} | Update tracked data for a day.
DELETE | /stats/{id} | Remove tracked data for a day.

### Front-End Specification

The front-end will be a single-page app using Backbone.js. The app will be served through the Python webserver, so you will have to put all your CSS and JavaScript in a directory called `/static/` and will have to make your `index.html` file as a Django template, which the Python students you're working with can help you do.

Registration and login can be on different pages than the main page if need be.

## Hard Mode

In addition to the requirements from **Normal Mode**:

* Users should be able to record different types of stats. You can choose the types, but here are some suggestions:
  * Clicker-style stats. The UI on these should change so you have a way to increase them by one via a button click. Good for tracking things as you're doing them.
  * Time-goal stats. The stat has a beginning value, ending value, and ending date. Track as normal, but you should be able to see if you're on track to meet your goal. Examples: weight loss, building up for a long run.
  * Yes-no stats. Did I do this today? This is often called the "Seinfeld calendar" or [chain calendar](http://chaincalendar.com/about).
  * Stats on a scale instead of unbounded. Example: On a scale of 1 to 5, what's my happiness level today?

* Make sure your interface [is responsive](https://developers.google.com/web/fundamentals/layouts/rwd-fundamentals/) and works well via mobile.

## Heroku instructions

This app should work well with Heroku as long as you run the following commands:

```
heroku config:set DJANGO_SETTINGS_MODULE=eager_viper.heroku_settings
heroku config:set PYTHONPATH=eager_viper
heroku config:set SECRET_KEY=$(date | md5 | base64)
```
