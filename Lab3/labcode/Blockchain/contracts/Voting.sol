pragma solidity ^0.4.17;


contract Voting {

    uint voteOpen;

    uint decided;

    address public director;

    mapping(address => Shareholder) public Shareholders;

    Choice[] public choices;

    struct Shareholder {
        uint canVote;
        bool voted;
        address identifier;
        uint answer;
        uint canSee;
    }

    struct Choice {
        bytes32 name;
        uint count;
    }

    event ShareholderAdded(
        address indexed _from,
        address indexed _holder
    );

    event ShareholderRemoved(
        address indexed _from,
        address indexed _holder
    );

    event QuestionAdded(
        address indexed _from,
        bytes32 indexed _question
    );

    modifier onlyDirector() {
        require(msg.sender == director);
        _;
    }

    function Voting() external {
        director = msg.sender;
        Shareholders[director].canVote = 1;
        Shareholders[director].canSee = 1;
        voteOpen = 1;
        decided = 0;
    }

    function addQuestion(bytes32 question) external onlyDirector {
        choices.push(Choice({
            name : question,
            count : 0
        }));
        QuestionAdded(msg.sender, question);
    }

    function addShareholder(address holder) external onlyDirector {
        require(!Shareholders[holder].voted && (Shareholders[holder].canVote == 0));
        Shareholders[holder].canVote = 1;
        ShareholderAdded(msg.sender, holder);
    }

    function removeShareholder(address holder) external onlyDirector {
        require(!Shareholders[holder].voted && (Shareholders[holder].canVote == 1));
        Shareholders[holder].canVote = 0;
        ShareholderRemoved(msg.sender, holder);
    }

    function vote(uint choiceNumber) external {
        Shareholder storage decider = Shareholders[msg.sender];
        require(!decider.voted);
        decider.voted = true;
        decider.answer = choiceNumber;
        choices[choiceNumber].count += decider.canVote;
    }

    function closeVoting() public onlyDirector {
        voteOpen = 0;
        decided = 1;
    }

    function kill() public onlyDirector {
        selfdestruct(director);
    }

    function voteDecision() public constant returns (bytes32 propName) {
        require(voteOpen == 0 && decided == 1);
        propName = voteWinner();
    }

    function voteCounts(uint ich) public constant returns (uint icnt) {
        icnt = choices[ich].count;
    }

    function voteWinner() private constant returns (bytes32 voteWin) {
        uint voteWinCount = 0;
        for (uint i = 0; i < choices.length; i++) {
            if (choices[i].count > voteWinCount) {
                voteWinCount = choices[i].count;
                voteWin = choices[i].name;
            }
        }
    }
}
