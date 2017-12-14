var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

console.log(web3.version.api);

var contract = "0x6ba6ccf8613f8cf0d8e36bc85b0fd05b5ba0109b";

var abi = [{
    "constant": true,
    "inputs": [{"name": "ich", "type": "uint256"}],
    "name": "voteCounts",
    "outputs": [{"name": "icnt", "type": "uint256"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
}, {
    "constant": false,
    "inputs": [],
    "name": "kill",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "constant": true,
    "inputs": [],
    "name": "director",
    "outputs": [{"name": "", "type": "address"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
}, {
    "constant": true,
    "inputs": [{"name": "", "type": "address"}],
    "name": "Shareholders",
    "outputs": [{"name": "canVote", "type": "uint256"}, {
        "name": "voted",
        "type": "bool"
    }, {"name": "identifier", "type": "address"}, {
        "name": "answer",
        "type": "uint256"
    }, {"name": "canSee", "type": "uint256"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
}, {
    "constant": true,
    "inputs": [],
    "name": "voteDecision",
    "outputs": [{"name": "propName", "type": "bytes32"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
}, {
    "constant": false,
    "inputs": [{"name": "holder", "type": "address"}],
    "name": "removeShareholder",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "constant": false,
    "inputs": [{"name": "question", "type": "bytes32"}],
    "name": "addQuestion",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "constant": false,
    "inputs": [],
    "name": "closeVoting",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "constant": false,
    "inputs": [{"name": "holder", "type": "address"}],
    "name": "addShareholder",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "constant": false,
    "inputs": [{"name": "choiceNumber", "type": "uint256"}],
    "name": "Vote",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "constant": true,
    "inputs": [{"name": "", "type": "uint256"}],
    "name": "choices",
    "outputs": [{"name": "name", "type": "bytes32"}, {
        "name": "count",
        "type": "uint256"
    }],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
}, {
    "inputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "constructor"
}, {
    "anonymous": false,
    "inputs": [{"indexed": true, "name": "_from", "type": "address"}, {
        "indexed": true,
        "name": "_holder",
        "type": "address"
    }],
    "name": "shareholderAdded",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{"indexed": true, "name": "_from", "type": "address"}, {
        "indexed": true,
        "name": "_holder",
        "type": "address"
    }],
    "name": "shareholderRemoved",
    "type": "event"
}, {
    "anonymous": false,
    "inputs": [{"indexed": true, "name": "_from", "type": "address"}, {
        "indexed": true,
        "name": "_question",
        "type": "bytes32"
    }],
    "name": "questionAdded",
    "type": "event"
}];

var MyContract = web3.eth.contract(abi);
console.log(web3.eth.accounts);
var myContractInstance = MyContract.at(contract);

// On a terminal you need to do the following
// run testrpc
// truffle compile
// truffle migrate
// inside truffle console run the following to intialize the constructor
// Voting.deployed(Voting)

myContractInstance.addQuestion("ABC", {from: web3.eth.accounts[0]});
myContractInstance.addQuestion("DEF", {from: web3.eth.accounts[0]});
myContractInstance.addQuestion("GHI", {from: web3.eth.accounts[0]});

for (var i = 1; i < 7; i++) {
    myContractInstance.addShareholder(web3.eth.accounts[i], {from: web3.eth.accounts[0]});
}

myContractInstance.Vote(1, {from: web3.eth.accounts[0]});
myContractInstance.Vote(1, {from: web3.eth.accounts[1]});
myContractInstance.Vote(1, {from: web3.eth.accounts[2]});
myContractInstance.Vote(1, {from: web3.eth.accounts[3]});
myContractInstance.Vote(2, {from: web3.eth.accounts[4]});
myContractInstance.Vote(2, {from: web3.eth.accounts[5]});
myContractInstance.closeVoting({from: web3.eth.accounts[0]});
console.log(myContractInstance.voteCounts(0));
console.log(myContractInstance.voteCounts(1));
console.log(myContractInstance.voteCounts(2));
console.log(myContractInstance.voteDecision().toString());

// On the terminal run nodejs main.js
// you should get the vote counts as
// 0
// 4
// 2
