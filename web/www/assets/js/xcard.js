var cardAPI = (function () {
	var API = {};
	var cardTemplate = _.loadTemplate('../template.html');

	function getCardInfo(code) {
		var card = {};
		var sampleImage = "../images/samples/portrait.jpg";
		switch(code) {
			case 1:
				card = {
					name: "Move Forward",
					desc: "Move the robot forward for 1 second.",
					image: sampleImage
				};
				break;
			case 2:
				card = {
					name: "Turn Left",
					desc: "Turn the robot 90 degrees to its left.",
					image: sampleImage
				};
				break;
			case 3:
				card = {
					name: "Turn Right",
					desc: "Turn the robot 90 degrees to its right.",
					image: sampleImage
				};
				break;
			case 4:
				card = {
					name: "Move Backwards",
					desc: "Move the robot backwards for one second.",
					image: sampleImage
				};
				break;
			case 5:
				card = {
					name: "Restart",
					desc: "Go back to the beginning of the program and start running it again.",
					image: sampleImage
				};
				break;
			case 6:
				card = {
					name: "Beep",
					desc: "Make the robot beep.",
					image: sampleImage
				};
				break;
			case 7:
				card = {
					name: "Left Bumper Start",
					desc: "This is paired with a 'Left Bumper End' card. Everything in between them will run whenever the left bumper is triggered.",
					image: sampleImage
				};
				break;
			case 8:
				card = {
					name: "Left Bumper End",
					desc: "This is paired with a 'Left Bumper Start' card. Everything in between them will run whenever the left bumper is triggered.",
					image: sampleImage
				};
				break;
			case 9:
				card = {
					name: "Right Bumper Start",
					desc: "This is paired with a 'Right Bumper End' card. Everything in between them will run whenever the right bumper is triggered.",
					image: sampleImage
				};
				break;
			case 10:
				card = {
					name: "Right Bumper End",
					desc: "This is paired with a 'Right Bumper Start' card. Everything in between them will run whenever the right bumper is triggered.",
					image: sampleImage
				};
				break;
			case 11:
				card = {
					name: "Wait",
					desc: "Let the robot take a break from all this exhausting moving, and let it sit for a second.",
					image: sampleImage
				};
				break;
			case 12:
				card = {
					name: "Blink Light",
					desc: "Blink. Blink.",
					image: sampleImage
				};
				break;
			case 13:
				card = {
					name: "Done",
					desc: "Why would you stop?",
					image: sampleImage
				};
				break;
			case 14:
				card = {
					name: "Dance",
					desc: "Robot breaks down into a mad dance sequence.",
					image: sampleImage
				};
				break;
			default:
				card = {
					name: "Unknown",
					desc: "Unknown",
					image: "http://bit.ly/1Qq2jVt"
				};
				break;
		}
		return card;
	}
	API.getCardInfo = getCardInfo;

	function jsonToCards(data, level, side) {
		side = side || '';
		level = level || 0;
		_.forEach(data, function (val, key) {
			var data = {};
			var element = {};
			if (key === 'main_list' && Array.isArray(val)) {
				_.forEach(val, function (code) {
					data = getCardInfo(code);
					data.bump = side || '';
					data.levl = level || 0;
					element = cardTemplate(data);
					$('#cards').append(element);
				});
			} else if (key === 'left_bumper' && val && typeof val === 'object') {
				data = getCardInfo(7);
				data.bump = side || '';
				data.levl = level || 0;
				element = cardTemplate(data);
				$('#cards').append(element);
				jsonToCards(val, level + 1, side + 'L');
				data = getCardInfo(8);
				data.bump = side || '';
				data.levl = level || 0;
				element = cardTemplate(data);
				$('#cards').append(element);
			} else if (key === 'right_bumper' && val && typeof val === 'object') {
				data = getCardInfo(9);
				data.bump = side || '';
				data.levl = level || 0;
				element = cardTemplate(data);
				$('#cards').append(element);
				jsonToCards(val, level + 1, side + 'R');
				data = getCardInfo(10);
				data.bump = side || '';
				data.levl = level || 0;
				element = cardTemplate(data);
				$('#cards').append(element);
			}
		});
	}
	API.jsonToCards = jsonToCards;

	return API;
}());
