pragma solidity^0.4.17;

contract Voting{

    uint voteOpen;
    uint Decieded;
    struct Shareholder{
        uint canVote;
        bool voted;
        address identifier;
        uint answer;
        uint canSee;
    }

    struct Choice{
        bytes32 name;
        uint count;
    }

    address public director;

    mapping(address => Shareholder) public Shareholders;
    Choice[] public choices;

    event shareholderAdded(
        address indexed _from,
        address indexed _holder
    );

    event shareholderRemoved(
        address indexed _from,
        address indexed _holder
    );

    event questionAdded(
            address indexed _from,
            bytes32 indexed _question
        );

    function Voting() public {
        director = msg.sender;
        Shareholders[director].canVote = 1;
        Shareholders[director].canSee = 1;
        voteOpen = 1;
        Decieded = 0;
    }
    //
    function addQuestion(bytes32 question) public{
        require(msg.sender == director);
        choices.push(Choice({
            name: question,
            count: 0
        }));
        questionAdded(msg.sender, question);
    }

    //
    function addShareholder(address holder) public {
        require((msg.sender == director) && !Shareholders[holder].voted && (Shareholders[holder].canVote == 0));
        Shareholders[holder].canVote = 1;
        shareholderAdded(msg.sender, holder);

    }
    //
    function removeShareholder(address holder) public {
        require((msg.sender!=director) && !Shareholders[holder].voted && (Shareholders[holder].canVote == 1));
        Shareholders[holder].canVote = 0;
        shareholderRemoved(msg.sender, holder);
    }

    function Vote(uint choiceNumber) public {
        Shareholder storage decider = Shareholders[msg.sender];
        require(!decider.voted);
        decider.voted=true;
        decider.answer = choiceNumber;
        choices[choiceNumber].count += decider.canVote;
    }
    //
    function voteWinner() private constant returns (bytes32 voteWin) {
        uint voteWinCount = 0;
        for(uint l=0; l<choices.length; l++){
            if(choices[l].count > voteWinCount){
                voteWinCount = choices[l].count;
                voteWin = choices[l].name;
            }
        }
    }

    function voteDecision() public constant returns (bytes32 propName){
        require(voteOpen == 0 && Decieded == 1);
        propName = voteWinner();
    }
    //
    function closeVoting() public {
        require(msg.sender == director);
        voteOpen = 0;
        Decieded = 1;
    }

    function voteCounts(uint ich) public constant returns(uint icnt){
        icnt = choices[ich].count;
    }

    function kill() public{
        if(msg.sender == director)
            selfdestruct(director);
   }

}
