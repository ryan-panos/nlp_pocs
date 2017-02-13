'use strict';

/* Controllers */

angular.module('Flaskular.controllers', [])
    .controller('HomeCtrl', [
        function() { }])
    .controller('ContactCtrl', [
        function() { }])
    .controller('FourOhFourCtrl', [
        function() { }]);

console.log(" LOADING!!! IbmCtrl!! ");

angular.module('Flaskular.controllers', ['Flaskular.services'])
    .controller('PeopleCtrl', ['$scope', '$log', 'Person',
        function ($scope, $log, Person) {
            var update = function () {
                Person.query({}, function(result) {
                    $scope.people = result.objects;
                });
            };

            $log.info("Querying people");
            update();

            $scope.save = function() {
                $log.info("Adding: ", $scope.search);
                var newper = new Person({'name': $scope.search});
                newper.$save();
                update();
            };


        }
                              ]);

angular.module('Flaskular.controllers', ['Flaskular.services'])
    .controller('IbmCtrl', ['$scope', '$log', 'TestIBMService',
        function ($scope, $log, TestIBMService) {
            $scope.ALL = "All";
            $scope.MANY = "Many";
            $scope.TARGET = "TARGET";
            $scope.OTHER = "Other";
            $scope.selectedMode = $scope.MANY;

            $scope.modes = [$scope.ALL, $scope.MANY,  $scope.OTHER];  //$scope.TARGET,

            $scope.DEFAULT_FILE = '<short default file>';
            $scope.ENV_FILE_10 = 'dataset_934_env_short.csv';
            $scope.ENV_FILE_1238 = 'dataset_840_env1.csv';
            $scope.selectedFile = $scope.DEFAULT_FILE;

            $scope.inputFiles = [$scope.DEFAULT_FILE, $scope.ENV_FILE_10, $scope.ENV_FILE_1238];


            console.log("INIT-ish selectedMode: ", $scope.selectedMode);


            $scope.onModeChange = function () {
                console.log("onModeChange selectedMode: ", $scope.selectedMode);

                // if ($scope.selectedMode == $scope.ALL) {
                //
                // } else if ($scope.selectedMode == $scope.MANY) {
                //
                // } else {
                //
                // }

                updatePage();
            };

            $scope.onFileChange = function () {
                console.log("onFileChange selectedFile: ", $scope.selectedFile);
                updatePage();
            };

            var updatePage = function() {

                if ($scope.selectedFile == $scope.DEFAULT_FILE) {
                    $scope.sentInputFile = '';
                } else {
                    $scope.sentInputFile = $scope.selectedFile;
                }

                if (!$scope.selectedMode || $scope.selectedMode == $scope.ALL ) {
                    $scope.mode_str = " Annnnd DOING Allll of IBM at once!! ";
                    $scope.loading_status = 'Calling IBM . ..';
                    //.<img class="blinking-cursor" src="static/img/blinking-cursor.gif-c200"/>
                    getAll();
                } else if ($scope.selectedMode == $scope.MANY) {
                    $scope.mode_str = " Annnnd DOING IBM in chunks ! ";
                    $scope.loading_status = 'Calling IBM . ...';
                    // <img class="blinking-cursor" src="static/img/blinking-cursor.gif-c200"/>
                    getMany();
                } else if ($scope.selectedMode == $scope.TARGET) {
                    $scope.mode_str = " Annnnd DOING the IBM services we are targeting ! ";
                    $scope.loading_status = 'Calling IBM . ...';
                    // <img class="blinking-cursor" src="static/img/blinking-cursor.gif-c200"/>
                    getMany();//todo !!!
                }
            };
            var getAll = function () {

                // TODO: maybe remove last?

                TestIBMService.queryAll({input_file: $scope.sentInputFile}, function(result) {

                    console.log(" >> GOT BACK: ", result);

                    $scope.big_res_ls = result;
                    $scope.loading_status = "";
                    // $scope.orginal_text = result["orginal_text"];

                    console.log(" >> $scope.big_res: ", $scope.big_res_ls);
                });
            };

            var getMany = function () {

                // TODO: maybe remove last?
                
                TestIBMService.queryMany({new_param: "bob", input_file: $scope.sentInputFile}, function(result) {

                    // console.log(" >> GOT BACK: ", result);

                    $scope.big_res_ls = result;
                    $scope.loading_status = "";
                    // $scope.orginal_text = result["orginal_text"];

                    console.log(" >> $scope.big_res: ", $scope.big_res_ls);
                    // console.log(" >> $scope.big_res[0]: ", $scope.big_res_ls[0]);
                });
            };

            var getTarget = function () {
                TestIBMService.queryTarget({}, function(result) {

                    console.log(" >> GOT BACK: ", result);

                    $scope.big_res_ls = result;
                    $scope.loading_status = "";
                    // $scope.orginal_text = result["orginal_text"];

                    console.log(" >> $scope.big_res: ", $scope.big_res_ls);
                });
            };


            $log.info("testing IBM! (this is init like . ...) ");
            updatePage()


        }
                              ]);

console.log("> DID  LOADING!!! IbmCtrl!! ");