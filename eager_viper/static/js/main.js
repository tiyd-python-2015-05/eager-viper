window.$ = require("jquery");
window.jQuery = $;
window._ = require("underscore");
var Backbone = require("backbone");
var PageableCollection = require("backbone.paginator");
require("bootstrap");

jQuery.fn.serializeObject = function () {
    var o = {}
    this.serializeArray().forEach(function (item) {
        if (o[item.name]) {
            if (typeof(o[item.name]) === "string") {
                o[item.name] = [o[item.name]];
            }
            o[item.name].push(item.value);
        } else {
            o[item.name] = item.value;
        }
    });
    return o;
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var Activity = Backbone.Model.extend({
    defaults: {
        title: ''
    }
});

var Activities = Backbone.Collection.extend({
    model: Activity,
    url: '/api/activities'
});

var Stat = Backbone.Model.extend({
    defaults: {
        count: 0
    },

    url: function () {
        if (this.id) {
            return "/api/stats/" + this.id;
        } else if (this.collection) {
            return this.collection.url();
        } else {
            return;
        }
    }
});

var Stats = Backbone.Collection.extend({
    initialize: function (models, options) {
        this.activityId = options.activity ? options.activity.id : options.activityId;
    },
    model: Stat,
    url: function () {
        return "/api/activities/" + this.activityId + "/stats";
    }
});


var ActivitiesView = Backbone.View.extend({
    initialize: function () {
        this.model.bind('add remove change', _.bind(this.render, this));
        this.stats = {};
        this.statsViews = {};
    },

    events: {
        'click .activity-heading': 'loadStats',
        'submit .new-activity-form': 'addActivity'
    },

    template: _.template($("#activity-list").html()),

    render: function () {
        this.$el.html(this.template({activities: this.model}));
        return this;
    },

    addActivity: function (event) {
        event.preventDefault();
        var $form = $(event.target);
        var activity = new Activity($form.serializeObject());
        this.model.create(activity);
    },

    loadStats: function (event) {
        var id = $(event.target).data('activityId');
        if (!this.stats[id]) {
            this.stats[id] = new Stats([], {activityId: id});
            this.stats[id].fetch();
        }
        if (!this.statsViews[id]) {
            var view = new StatsView({
                el: $("#collapse-" + id + " .panel-body"),
                model: this.stats[id]
            });
            view.render();
        }
    }
});

var StatsView = Backbone.View.extend({
    initialize: function () {
        this.model.bind('add remove change', _.bind(this.render, this));
    },

    events: {
        'submit .new-stat-form': 'addStat',
        'click .glyphicon-remove': 'removeStat'
    },

    template: _.template($("#stat-list").html()),

    render: function () {
        this.$el.html(this.template({stats: this.model}));
        return this;
    },

    addStat: function (event) {
        event.preventDefault();
        var $form = $(event.target);
        var stat = new Stat($form.serializeObject());
        this.model.create(stat);
    },

    removeStat: function (event) {
        var id = $(event.target).data('statId');
        var stat = this.model.get([id]);
        stat.destroy();
    }
});

var activities = new Activities();
activities.fetch();
var view = new ActivitiesView({
    el: $("#main"),
    model: activities
});
view.render();


console.log("Howdy from main.js!");