//Require Mongoose
var mongoose = require('mongoose');

//Define a schema
var Schema = mongoose.Schema;

var CompanySchema = new Schema({
    name: String,
    stream: [String],
    date_of_arrival: Date,
    cgpa_cutoff: Number
});

// Compile model from schema
var CompaniesModel = mongoose.model('Companies',  CompanySchema);