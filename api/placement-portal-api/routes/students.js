var express = require('express');
var router = express.Router();

var StudentModel = require('../models/student');

/* GET students listing. */
router.get('/', function(req, res, next) {
  StudentModel.find((err, dbRes) => {
    if (err) next(err);
    res.send(dbRes);
  });
});

/* GET students listing. */
router.get('/:studentId', function(req, res, next) {
  var studentId = req.params["studentId"];
  StudentModel.findById(studentId, (err, dbRes) => {
    if (err) next(err);
    res.send(dbRes || {});
  });
});

/* GET students listing. */
router.get('/name/:studentName', function(req, res, next) {
  var studentName = req.params["studentName"];
  StudentModel.find({name: studentName}, (err, dbRes) => {
    if (err) next(err);
    res.send(dbRes);
  });
});

module.exports = router;
