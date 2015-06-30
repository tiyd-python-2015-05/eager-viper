window.$ = require("jquery");
window.jQuery = $;
window._ = require("underscore");
var Backbone = require("backbone");
var PageableCollection = require("backbone.paginator");
require("bootstrap");

var Activity = Backbone.Model.extend({
    defaults: {
        title: ''
    }
});

var Activities = Backbone.Collection.extend({
    model: Activity,
    url: '/api/activities'
});


var ActivityView = Backbone.View.extend({
    template: _.template($("#activity-detail").html()),
    render: function () {
        this.$el.html(this.template(this.model.attributes));
        return this;
    }
});

var ActivitiesView = Backbone.View.extend({
    initialize: function () {
        this.model.bind('add remove change', _.bind(this.render, this));
    },

    template: _.template($("#activity-list").html()),

    render: function () {
        activities = this.model.map(function (activity) {
            var view = new ActivityView({model: activity});
            return view.render().$el.html();
        });

        this.$el.html(this.template({activities: activities}));
        return this;
    }
});

var activities = new Activities();
activities.fetch();
var view = new ActivitiesView({
    el: $("#main"),
    model: activities});
view.render();




console.log("Howdy from main.js!");