module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            dist: {
                src: [
                    'static/js/*.js' // All JS files in the JS folder
                ],
                dest: 'static/js/production.js',
            }
        },

        uglify: {
            build: {
                src: 'static/js/production.js',
                dest: 'static/js/production.min.js'
            }
        },

        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'static/images/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'static/images/'
                }]
            }
        },

        watch: {
            options: {
                livereload: true,
            },

            scripts: {
                files: ['static/js/*.js'],
                tasks: ['concat', 'uglify'],
                options: {
                    spawn: false,
                },
            },

            css: {
                files: ['static/css/*.scss'],
                tasks: ['sass'],
                options: {
                    spawn: false,
                },
            },
        },

        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: {
                    'static/css/global.css': 'static/css/global.scss'
                }
            }
        }
    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['concat', 'uglify', 'imagemin', 'sass', 'watch']);

};