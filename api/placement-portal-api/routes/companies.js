var express = require('express');
var router = express.Router();

var companyModel = require('../models/company') 

/* GET companies listing. */
router.get('/', function(req, res, next) {
  companyModel.find((err, dbRes)=>{
    res.send(dbRes);
  });
});

/* GET companies listing. */
router.get('/:companyId', function(req, res, next) {
  var companyId = req.params["companyId"];

  res.send('respond with companyId : ' + companyId);
});

/* GET companies listing. */
router.get('/name/:companyName', function(req, res, next) {
  var companyName = req.params["companyName"]

  res.send('respond with companyName : ' + companyName);
});

module.exports = router;
