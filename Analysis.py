from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Image
import database.Classifier
import database.AnalysisResult
from models.Analysis import Analysis as AnalysisModel
from models.AnalysisResult import AnalysisResult as AnalysisResultModel
from repository.base import Base


class Analysis(Base.Base):
    __tablename__ = 'analysis'

    id = Column(Integer, primary_key=True)
    idImage = Column('id_image', Integer, ForeignKey('images.id'))
    idClassifier = Column(
        'id_classifier',
        Integer,
        ForeignKey('classifiers.id'))
    image = relationship('Image', back_populates='analysis')
    classifier = relationship('Classifier', back_populates='analysis')
    analysis_results = relationship('database.AnalysisResult.AnalysisResult',
                                    lazy='subquery',
                                    back_populates='analysis')

    def __init__(self,
                 id=0,
                 idImage=0,
                 image=object(),
                 idClassifier=0,
                 classifier=object(),
                 analysis=AnalysisModel(),
                 analysis_results=AnalysisResultModel()):
        if (analysis.id or analysis.image.id or analysis.classifier.id):
            self.id = analysis.id
            self.idImage = analysis.image.id
            self.idClassifier = analysis.classifier.id
            self.analysis_results = []
            for result in analysis_results:
                self.analysis_results.append(
                    database.AnalysisResult.AnalysisResult(result))
        else:
            self.id = id
            self.idImage = idImage
            self.idClassifier = idClassifier
            self.analysis_results = analysis_results
