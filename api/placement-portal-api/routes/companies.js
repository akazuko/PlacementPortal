var express = require('express');
var router = express.Router();

var companyModel = require('../models/company') 

/* GET companies listing. */
router.get('/', function(req, res, next) {
  companyModel.find((err, dbRes) => {
    if (err) next(err);
    res.send(dbRes);
  });
});

/* GET companies listing. */
router.get('/:companyId', function(req, res, next) {
  var companyId = req.params["companyId"];
  companyModel.findById(companyId, (err, dbRes) => {
    if (err) next(err);
    res.send(dbRes || {});
  });
});

/* GET companies listing. */
router.get('/name/:companyName', function(req, res, next) {
  var companyName = req.params["companyName"];
  companyModel.find({name: companyName}, (err, dbRes) => {
    if (err) next(err);
    res.send(dbRes);
  });
});

module.exports = router;
