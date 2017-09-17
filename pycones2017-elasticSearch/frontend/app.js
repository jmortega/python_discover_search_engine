var myApp = angular.module("myApp", ["ngRoute", "ngResource", "myApp.services"]);

var services = angular.module("myApp.services", ["ngResource"])
services
.factory('Talk', function($resource) {
    return $resource('http://localhost:5000/api/v1/talks/:id', {id: '@id'}, {
        get: { method: 'GET' },
        delete: { method: 'DELETE' }
    });
})
.factory('Talks', function($resource) {
    return $resource('http://localhost:5000/api/v1/talks', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST', }
    });
})
.factory('Types', function($resource) {
    return $resource('http://localhost:5000/api/v1/types/:id', {id: '@id'}, {
        get: { method: 'GET' }
    });
})
.factory('Type', function($resource) {
    return $resource('http://localhost:5000/api/v1/types', {}, {
        query: { method: 'GET', isArray: true}
    });
})
.factory('Search', function($resource) {
    return $resource('http://localhost:5000/api/v1/search', {q: '@q'}, {
        query: { method: 'GET', isArray: true}
    });
});

myApp.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'pages/main.html',
        controller: 'mainController'
    })
    .when('/newTalk', {
        templateUrl: 'pages/talk_new.html',
        controller: 'newTalkController'
    })
    .when('/talks', {
        templateUrl: 'pages/talks.html',
        controller: 'talkListController'
    })
    .when('/talks/:id', {
        templateUrl: 'pages/talk_details.html',
        controller: 'talkDetailsController'
    })
});

myApp.filter('filterTypes', function() {
  return function(input) {
    var output = new Array();
    for (i=0; i<input.length; i++) {
        if (input[i].checked == true) {
            output.push(input[i].name);
        }
    }
    return output;
  }
});

myApp.controller(
    'mainController',
    function ($scope, Search) {
        $scope.search = function() {
            q = $scope.searchString;
            if (q.length > 1) {
                $scope.results = Search.query({q: q});    
            }
        };
    }
);

myApp.controller(
    'newTalkController',
    function ($scope, Types, Talks, $location, $timeout, $filter) {
        $scope.types = Types.query();
        $scope.insertTalk = function () {
            $scope.talk.types = $filter('filterTypes')($scope.types);
            Talks.create($scope.talk);
            $timeout(function (){
                $location.path('/talks').search({'created': $scope.talk.title});    
            }, 500);
        };
        $scope.cancel = function() {
            $location.path('/talks');
        };
    }
    
);

myApp.controller(
    'talkListController',
    function ($scope, Talks, Talk, $location, $timeout) {
        if ($location.search().hasOwnProperty('created')) {
            $scope.created = $location.search()['created'];
        }
        if ($location.search().hasOwnProperty('deleted')) {
            $scope.deleted = $location.search()['deleted'];
        }
        $scope.deleteTalk = function(talk_id) {
            var deleted = Talk.delete({id: talk_id});
            $timeout(function(){
                $location.path('/talks').search({'deleted': 1})
            }, 500);
        };
        $scope.talks = Talks.query();
    }
);

myApp.controller(
    'talkDetailsController', ['$scope', 'Talk', '$routeParams',
    function ($scope, Talk, $routeParams) {
        $scope.talk = Talk.get({id: $routeParams.id});
    }
]);


