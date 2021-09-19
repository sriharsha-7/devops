from pr_reporter.models.pr_models import PrInfo
from pr_reporter.pr import PR
import argparse
import logging


def collect_arguments() -> PrInfo:
    parser = argparse.ArgumentParser(prog='Pull Requests Reporter', formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('--email', type=str)
    parser.add_argument('--repo', type=str, default='scikit-learn')
    parser.add_argument('--owner', type=str, default='scikit-learn')
    args = parser.parse_args()
    pr_info = PrInfo(repo=args.repo, email=args.email, owner=args.owner)
    return pr_info

def setup_logger(filename):
    
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=filename,
                        filemode='a')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger().addHandler(console)


def main(pr_info: PrInfo):
    pr_obj = PR(pr_info)
    pr_obj.run()
    

if __name__ == "__main__":
    
    log_file = "pr.log"
    setup_logger(log_file)
    args = collect_arguments()
    main(args)

    