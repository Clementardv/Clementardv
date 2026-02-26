freeStyleJob('example') {
    label('CentOSNode1')
    scm {
      git {
        branch('*/main')
        remote {
          url('git@github.com:Clementardv/Clementardv.git')
          credentials('github-ssh-key')
        }
      }
    }
    steps {
      shell {
        command("""#!/bin/bash
# On installe pylint localement pour l'utilisateur clement sans sudo
pip3 install pylint --user --quiet

echo "--- ANALYSE DE QUALITE ---"
# On lance l'analyse (change le '.' par le nom du fichier pour tes tests)
python3 check_quality.py .""")
      }
    }
}
