var Ballot = artifacts.require("./Voting.sol");
module.exports = function(deployer) {
	deployer.deploy(Ballot);
};
