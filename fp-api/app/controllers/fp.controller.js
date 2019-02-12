var fs = require('fs');

var falsepositives = {}

loadData = function () {
    fs.readFile('data.json', 'utf8', function readFileCallback(err, data) {
        if (err) {
            console.log(err);
        } else {
            if(data === '') {
                data = '{}';
            }
            falsepositives = JSON.parse(data);
        }
    });
}

writeData = function () {
    var json = JSON.stringify(falsepositives);
    fs.writeFile('data.json', json, 'utf8', function writeFileCallback(err, data) {
		if (err) {
            console.log(err);
        } else {
			loadData();
		}
	});
}

loadData();

exports.findAll = function (req, res) {
    console.log("findAll: \n" + JSON.stringify(falsepositives, null, 4));
    res.end(JSON.stringify(falsepositives, null, 4));
};

exports.findOne = function (req, res) {
    console.log("findOne: \n" + req.params.id);
	
    var fp = falsepositives[req.params.id];
    console.log("findOne: \n" + JSON.stringify(fp, null, 4));
    res.end(JSON.stringify(fp, null, 4));
};

exports.updateOrCreate = function (req, res) {
    var postedFP = req.body;

    console.log("updateOrCreate: \n" + postedFP.id);
	
    falsepositives[postedFP.id] = postedFP;

    writeData();

    console.log("updateOrCreate: \n" + JSON.stringify(postedFP, null, 4));
    res.end(JSON.stringify(postedFP, null, 4));
};

exports.delete = function (req, res) {
    console.log("delete: \n" + req.params.id);
	delete falsepositives[req.params.id];
	
    writeData();

    res.end("deleted: \n" + req.params.id);
};