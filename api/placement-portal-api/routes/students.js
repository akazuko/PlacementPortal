var express = require('express');
var router = express.Router();

/* GET students listing. */
router.get('/', function(req, res, next) {
  res.send('respond with all');
});

/* GET students listing. */
router.get('/:studentId', function(req, res, next) {
  var studentId = req.params["studentId"];

  res.send('respond with studentId : ' + studentId);
});

/* GET students listing. */
router.get('/name/:studentName', function(req, res, next) {
  var studentName = req.params["studentName"];

  res.send('respond with studentName : ' + studentName);
});

module.exports = router;
