/*

All validation would happen on client side.
Password would comehash from client side.
Structureis public,private or partnerhip
*/

const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const axios = require('axios');

const Company = require("../models/company");
const Farmer = require("../models/farmer");
const CropToGrow = require("../models/croptobegrown");

router.get("/",(req, res, next) => {
	res.send("Hello welcome to agri basket api");
});

router.get("/predictCrop",(req,res,next) => {
	axios.post('https://agrobasketpreiction.herokuapp.com/predictKNeighborsRegressor', {
    soil : "Alluvial Soil",
	season : "Kharif",
	month :"May",
	mintemp: "22",
	maxtemp :"32",
	soilPhMin: "5",
	soilPhMax :"7",
	minRainfall: "1750",
	maxRainfall :"3000"
  })
  .then(axiosRes => {
	let cropName = (axiosRes.data).toLowerCase();
	console.log(cropName);
	if(cropName != "None"){
		CropToGrow.aggregate([
		{
			$lookup:{
				from : 'companies',
				localField : 'company',
				foreignField: '_id',
	         	as: 'companydetail'
			}
		},{
			$match:{
				cropname: cropName,
				status: "Not accepted",
			}
		}
		]).exec(function(err, cp) {
	    	if(cp.length == 0){
	    		res.send("No match found for given crop");
	    	}
	    	else
	    		res.send(cp);
		});
	}
  })
  .catch(error => {
    console.error(error)
  })
});

router.get("/getAllCompany",(req,res,next) => {

	Company.find({}, (err,matched) => {
		if(err){
            console.log("Herereee");
            res.status(404).json({msg: "Error  " + err})
        }else{
            res.send(matched);
        }
	})

});

router.get("/getAllFarmer",(req,res,next) => {

	Farmer.find({}, (err,matched) => {
		if(err){
            console.log("Herereee");
            res.status(404).json({msg: "Error  " + err})
        }else{
            res.send(matched);
        }
	})

});

router.get("/addCompany/:name/:address/:founder/:emailid/:phoneno/:structure/:avgturnover/:password",(req,res,next) => {
	let nameP = req.params['name'];
	let addressP = req.params['address'];
	let founderP = req.params['founder'];
	let emailidP = req.params['emailid'];
	let phonenoP = req.params['phoneno'];
	let structureP = req.params['structure'];
	let avgturnoverP = req.params['avgturnover'];
	let passwordP = req.params['password'];
	
	Company.find({ name : nameP}, (err,matched) => {
		if(err){
            console.log("Herereee");
            res.status(404).json({msg: "Error  " + err})
        }else if(matched.length == 0){
            let newCmpany = new Company({
		        name : nameP,
				address : addressP,
				founder : founderP,
				emailid : emailidP,
				phoneno : phonenoP,
				structure : structureP,
				avgturnover : avgturnoverP,
				password : passwordP
		    });
		    newCmpany.save((err, notes)=>{
		        if(err){
		            res.json({msg: "Failed to add a company"+err})
		        }else{
		            res.json({msg: "Company Added successfully"})
		        }
		    });
        }else{
            res.send("Already the company was registered");
        }
	})	
});


router.get("/addFarmer/:name/:address/:phoneno/:username/:password",(req,res,next) => {
	let nameP = req.params['name'];
	let addressP = req.params['address'];
	let phonenoP = req.params['phoneno'];
	let usernameP = req.params['username'];
	let passwordP = req.params['password'];
	
	Farmer.find({ username : usernameP}, (err,matched) => {
		if(err){
            console.log("Herereee");
            res.status(404).json({msg: "Error  " + err})
        }else if(matched.length == 0){
            let newFarmer = new Farmer({
		        name : nameP,
				address : addressP,
				phoneno : phonenoP,
				username : usernameP,
				password : passwordP
		    });
		    newFarmer.save((err, notes)=>{
		        if(err){
		            res.json({msg: "Failed to add a company"+err})
		        }else{
		            res.json({msg: "Farmer Added successfully"})
		        }
		    });
        }else{
            res.send("username is already taken");
        }
	})	
});

router.get("/checkCompanyLogin/:emailid/:password" ,(req,res,next) => {
	let emailidP = req.params['emailid'];
	let passwordP = req.params['password'];
	Company.find({ emailid : emailidP}, (err,matched) => {
		if(err){
            console.log("Herereee");
            res.status(404).json({msg: "Error  " + err})
        }else if(matched.length == 0){
            res.send("Email id was not registered");
        }else{
        	if(matched[0].password == passwordP)
            	res.send(matched[0]);
            else
            	res.send("password didnt matched");
        }
	})

});

router.get("/checkFarmerLogin/:username/:password" ,(req,res,next) => {
	let usernameP = req.params['username'];
	let passwordP = req.params['password'];
	Farmer.find({ username : usernameP}, (err,matched) => {
		if(err){
            console.log("Herereee");
            res.status(404).json({msg: "Error  " + err})
        }else if(matched.length == 0){
            res.send("username was not registered");
        }else{
        	if(matched[0].password == passwordP)
            	res.send(matched[0]);
            else
            	res.send("password didnt matched");
        }
	})

});

router.get("/updateStatus/:cropToGrowId/:status", (req,res,next) => {
	let cropToGrowIdP = req.params['cropToGrowId'];
	let statusP = req.params['status'];
	CropToGrow.findOneAndUpdate({ _id: new mongoose.Types.ObjectId(cropToGrowIdP) }, { status: statusP }, function(err,result) {
		if (err) {
			res.send(err);
		} else {
			res.send(result);
		}
	});
});

router.get("/updateStatusandFarmerId/:cropToGrowId/:status/:farmerId", (req,res,next) => {
	let cropToGrowIdP = req.params['cropToGrowId'];
	let statusP = req.params['status'];
	let farmerIdP = req.params['farmerId'];
	CropToGrow.findOneAndUpdate({ _id: new mongoose.Types.ObjectId(cropToGrowIdP) }, { status: statusP, farmer: new mongoose.Types.ObjectId(farmerIdP) }, function(err,result) {
		if (err) {
			res.send(err);
		} else {
			res.send(result);
		}
	});
});


router.get("/getCropStatus/:companyId", (req,res,next) => {
	let companyIdP = req.params['companyId'];
	CropToGrow.aggregate([
	{
		$lookup:{
			from : 'farmers',
			localField : 'farmer',
			foreignField: '_id',
         	as: 'farmerdetail'
		}
	},{
		$match:{
			company: new mongoose.Types.ObjectId(companyIdP),
		}
	}
	]).exec(function(err, cp) {
    	res.send(cp);
	});
});

router.get("/getCrop/:cropname", (req,res,next) => {
	let cropP = req.params['cropname'];
	CropToGrow.aggregate([
	{
		$lookup:{
			from : 'companies',
			localField : 'company',
			foreignField: '_id',
         	as: 'companydetail'
		}
	},{
		$match:{
			cropname: cropP
		}
	}
	]).exec(function(err, cp) {
    	if(cp.length == 0){
    		res.send("No match found for given crop");
    	}
    	else
    		res.send(cp);
	});
});


router.get("/addCrop/:cid/:name/:cropname/:totalproduce/:price/:startdate/:enddate/:status", (req,res,next) => {

	let companyP = req.params['cid'];
	let nameP = req.params['name'];
	let cropnameP = req.params['cropname'];
	let totalproduceP = req.params['totalproduce'];
	let priceP = req.params['price'];
	let startdateP = req.params['startdate'];
	let enddateP = req.params['enddate'];
	let statusP = req.params['status'];

	let newCrop = new CropToGrow({
        company : companyP,
		name : nameP,
		cropname : cropnameP,
		totalproduce : totalproduceP,
		price : priceP,
		startdate : startdateP,
		enddate : enddateP,
		status: statusP
    });
    newCrop.save((err, notes)=>{
        if(err){
            res.json({msg: "Failed to add a company"+err})
        }else{
            res.json({msg: "Crop Added successfully"})
        }
    });
});

module.exports = router;