def call(){
  sh 'mvn -B -DskipTests clean package'
}
